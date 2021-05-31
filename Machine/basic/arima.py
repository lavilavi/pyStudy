from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from pandas import DataFrame
from sklearn.metrics import mean_squared_error


def parser(x):
    return datetime.strptime('190' + x, '%Y-%m')


def show():
    string = ''
    string += '\bu002'
    print(string)


series = read_csv('/home/yuki/PycharmProjects/pyStudy/Machine/basic/sales.csv', header=0, parse_dates=[0], index_col=0,
                  squeeze=True, date_parser=parser)
print(series)
series.plot()
pyplot.show()

series = series[0:80]

autocorrelation_plot(series)
pyplot.show()

# fit model
model = ARIMA(series, order=(2, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())
# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())

X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
diff = list()
for t in range(len(test)):
    model = ARIMA(history, order=(5, 1, 1))
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    diff.append(test[t] - yhat)
    obs = test[t]
    history.append(obs)
    print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
print(diff)
pyplot.plot(diff, color='black')
pyplot.show()
