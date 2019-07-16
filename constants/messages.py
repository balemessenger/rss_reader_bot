class BotMessage:
    invalid_username = "قالب آیدی وارد شده معتبر نیست!"
    rss_added_successfully = "فیدخوان شما با *موفقیت* اضافه گردید."
    no_rss = "هیچ فیدخوانی یافت نشد!"
    remove_success = "فیدخوان مورد نظر با موفقیت حذف شد!"
    select_rss = "فیدخوان مورد نظر برای *حذف* را انتخاب کنید:"
    start = "من بازوی فیدخوان هستم.\n" \
            "شما می‌توانید با استفاده از من به راحتی محتوای سایت‌هایی" \
            " که از امکان RSS پشتیبانی می‌کنند را در کانال دلخواه خود در بله مشاهده کنید."
    not_permitted = "شما مجاز به انجام این کار نیستید!"
    enter_rss_url = "شما مجاز شناخته شدید. لطفا آدرس فیدخوان را وارد کنید:"
    enter_channel_id = "آی‌دی کانال خود در بله انتخاب یا وارد کنید.\n" \
                       "(مثال: @Balechannel)\n" \
                       "فید سایت‌های انتخابی شما در این کانال قرار خواهد گرفت.\n\n" \
                       "*توجه مهم:* شما باید این بازو را در کانال خود اضافه کرده و *ادمین* کنید." \
                       " همچنین خودتان هم ادمین باشید."
    help = "راهنما"
    line = "\n"


class Keyboards:
    get_rss_list = "فیدخوان های من"
    remove_rss = "پاک کردن فیدخوان"
    check = "احراز هویت"
    back_to_main = "بازگشت به منوی اصلی"
    manage_rss = "مدیریت فیدخوان"
    create_rss = "تعریف فیدخوان"
    start = "شروع"
    report = "گزارش"
    yes = "بله"
    guide = "راهنما"


class UserData:
    total_price = "total_price"


class ConversationStates:
    NICK_NAME, RSS, PRODUCT_INFO, PRODUCT, CONFIRM_ORDER, PRODUCT_ADDED_TO_ORDER, PAYMENT, PRODUCT_COUNT = range(8)
