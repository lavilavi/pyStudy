import numpy as np
from sklearn.cluster import KMeans
import Machine.basic.ekg_data as ekg_data
import matplotlib.pyplot as plt
import learn_utils

segment_len = 32
slide_len = 2

if __name__ == '__main__':
    segments = []
    ekg_filename = 'a02.dat'
    ekg_data = ekg_data.read_ekg_data(ekg_filename)
    print(ekg_data.shape)

    print("ekg_data[0]:\t", ekg_data[0])
    print("ekg_data[1]:\t", ekg_data[1])
    print("ekg_data.min:\t", ekg_data.min())
    print("ekg_data.max:\t", ekg_data.max())

    n_samples_to_plot = 1000
    plt.plot(ekg_data[0:n_samples_to_plot])
    plt.xlabel("Sample number")
    plt.ylabel("Signal value")
    plt.title("Sample plots")
    plt.show()

    ekg_data = ekg_data[0:8192]
    # Make data incremental
    for i in range(0, len(ekg_data), 100):
        ekg_data[i:i + 100] += 25 * i / 100
    plt.plot(ekg_data[0:n_samples_to_plot])
    plt.xlabel("Sample number")
    plt.ylabel("Signal value")
    plt.title("Sample plots")
    plt.show()

    ekg_data_anomalous = np.copy(ekg_data)
    for start_pos in range(0, len(ekg_data), slide_len):
        end_pos = start_pos + segment_len
        segment = np.copy(ekg_data[start_pos:end_pos])
        # if we're at the end and we've got a truncated segment, drop it
        if len(segment) != segment_len:
            continue
        segments.append(segment)

    print("Produced %d waveform segments" % len(segments))

    learn_utils.plot_waves(segments, 3, "First waveform")

    window_rads = np.linspace(0, np.pi, segment_len)
    window = np.sin(window_rads) ** 2

    plt.plot(window)
    plt.title("Windows")
    plt.show()

    windowed_segments = []
    for segment in segments:
        windowed_segment = np.copy(segment) * window
        windowed_segments.append(windowed_segment)

    learn_utils.plot_waves(windowed_segments, 3, "")

    clusterer = KMeans(n_clusters=1050)
    clusterer.fit(windowed_segments)

    learn_utils.plot_waves(clusterer.cluster_centers_, 1, "Clusters")

    slide_len = segment_len / 2
    test_segments = learn_utils.sliding_chunker(
        ekg_data,
        window_len=segment_len,
        slide_len=int(slide_len)
    )

    centroids = clusterer.cluster_centers_

    segment = np.copy(test_segments[0])
    # remember, the clustering was set up using the windowed data
    # so to find a match, we should also window our search key
    windowed_segment = segment * window
    # predict() returns a list of centres to cope with the possibility of multiple
    # samples being passed
    nearest_centroid_idx = clusterer.predict([windowed_segment])[0]
    nearest_centroid = np.copy(centroids[nearest_centroid_idx])
    plt.figure()
    plt.plot(segment, label="Original segment")
    plt.plot(windowed_segment, label="Windowed segment")
    plt.plot(nearest_centroid, label="Nearest centroid")
    plt.legend()
    plt.title("Centroids")
    plt.show()

    reconstruction = np.zeros(len(ekg_data))
    slide_len = segment_len / 2

    for segment_n, segment in enumerate(test_segments):
        # don't modify the data in segments
        segment = np.copy(segment)
        segment *= window
        nearest_centroid_idx = clusterer.predict([segment])[0]
        centroids = clusterer.cluster_centers_
        nearest_centroid = np.copy(centroids[nearest_centroid_idx])

        # overlay our reconstructed segments with an overlap of half a segment
        pos = int(segment_n * slide_len)
        reconstruction[pos:pos + segment_len] += nearest_centroid

    n_plot_samples = 1000

    error = reconstruction[0:n_plot_samples] - ekg_data[0:n_plot_samples]
    error_98th_percentile = np.percentile(error, 98)
    print("Maximum reconstruction error was %.1f" % error.max())
    print("98th percentile of reconstruction error was %.1f" % error_98th_percentile)

    plt.plot(ekg_data[10:n_plot_samples], label="Original EKG")
    plt.plot(reconstruction[10:n_plot_samples], label="Reconstructed EKG")
    plt.plot(error[10:n_plot_samples], label="Reconstruction Error")
    plt.legend()
    plt.show()

    ekg_data_anomalous = np.copy(ekg_data)
    ekg_data_anomalous[210:215] = 0

    recontruction = \
        learn_utils.reconstruct(ekg_data_anomalous, window, clusterer)

    error = reconstruction[0:n_plot_samples] - ekg_data_anomalous[0:n_plot_samples]
    error_98th_percentile = np.percentile(error, 98)
    print("Maximum reconstruction error was %.1f" % error.max())
    print("98th percentile of reconstruction error was %.1f" % error_98th_percentile)

    plt.plot(ekg_data_anomalous[0:n_plot_samples], label="Original EKG")
    plt.plot(reconstruction[0:n_plot_samples], label="Reconstructed EKG")
    plt.plot(error[0:n_plot_samples], label="Reconstruction Error")
    plt.legend()
    plt.show()
