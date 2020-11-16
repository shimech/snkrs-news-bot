class Message:
    snkrs_pass_message = "<!channel> 【SNKRS PASS News!!】" + "\n"
    snkrs_pass_message += "{}" + "\n"
    snkrs_pass_message += "のSNKRS PASSが発行されました！急げ！！:snkrspass:" + "\n"
    snkrs_pass_message += "{}" + "\n"

    normal_news_message = "<!channel> 【New Post】" + "\n"
    normal_news_message += "{}" + "\n"
    normal_news_message += "の新規情報が投稿されました。:snkrs:" + "\n"
    normal_news_message += "{}" + "\n"

    @classmethod
    def make_message(cls, name, url, is_snkrs_pass):
        base_message = cls.snkrs_pass_message if is_snkrs_pass else cls.normal_news_message
        return base_message.format(name, url)
