import ujson as json
class tags():
    def __init__(self):
        self.refresh()
        self.auto_save = True

    def refresh(self):
        with open('./data/tags.json') as file:
            self.data = json.loads(file.read())

    def save(self):
        with open('./data/tags.json','w') as file:
            file.write(json.dumps(self.data))

    def __auto_save(self):
        if self.auto_save:
            self.save()

    def add_tag(self,tag_name):
        self.data['tags'].append(tag_name)
        self.data['tags-article'][tag_name] = []
        self.__auto_save()

    def add_article(self,tag_name,article_path):
        if tag_name in self.data['tags']: #检查tag是否存在
            self.data['tags-article'][tag_name] = article_path # 如果存在，添加进列表
        else:
            self.add_tag(tag_name) #不存在，添加进去
            self.add_article(tag_name, article_path) #重新添加
        self.__auto_save()

if __name__ == "__main__":
    test = tags()
    print(test.data)
    test.add_article("first_tag", "test")