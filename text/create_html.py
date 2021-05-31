detail_pre = '<div data-v-4f100e37="" class="el-form-item el-form-item--mini"><label class="el-form-item__label" style="width: 140px;"><span data-v-4f100e37="" class="color8d">'
detail_middle = '</span></label><div class="el-form-item__content" style="margin-left: 140px;"><span data-v-4f100e37="" class=" size-14 col59646D">'
detail_post = '</span><!----></div></div>'

add_pre = '<div data-v-3108fdd4="" class="el-form-item is-required el-form-item--mini"><label for="planCode" class="el-form-item__label" style="width: 140px;">'
add_middle = '</label><div class="el-form-item__content" style="margin-left: 140px;"><div data-v-3108fdd4="" class="w-168 el-input el-input--mini el-input--suffix"><!----><input type="text" autocomplete="off" placeholder="'
add_post = '" class="el-input__inner"><!----><!----><!----><!----></div><!----></div></div>'


def add_items(item_name):
    print(add_pre + item_name + add_middle + item_name + add_post)


def detail_items():
    print(detail_pre + detail_middle + detail_post)


if __name__ == '__main__':
    f = open('lis.txt')
    items = f.readlines()
    for item in items:
        add_items(item.rstrip())
