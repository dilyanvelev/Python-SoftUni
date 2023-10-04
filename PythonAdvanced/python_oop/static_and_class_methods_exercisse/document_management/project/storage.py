# from python_oop.static_and_class_methods_exercisse.document_management.project.category import Category
# from python_oop.static_and_class_methods_exercisse.document_management.project.document import Document
# from python_oop.static_and_class_methods_exercisse.document_management.project.topic import Topic


from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = next(filter(lambda c: c.id == category_id, self.categories))
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = next(filter(lambda t: t.id == topic_id, self.topics))

        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = next(filter(lambda d: d.id == document_id, self.documents))

        document.file_name = new_file_name

    def delete_category(self, category_id):
        for category in self.categories:
            if category_id == category.id:
                self.categories.remove(category)

    def delete_topic(self, topic_id):
        for topic in self.topics:
            if topic_id == topic.id:
                self.topics.remove(topic)

    def delete_document(self, document_id):
        for document in self.documents:
            if document_id == document.id:
                self.documents.remove(document)

    def get_document(self, document_id):
        document = next(filter(lambda d: d.id == document_id, self.documents))
        return document

    def __repr__(self):
        documents = [str(document) for document in self.documents]

        return '\n'.join(documents)



# c1 = Category(1, "work")
# t1 = Topic(1, "daily tasks", "C:\\work_documents")
# d1 = Document(1, 1, 1, "finilize project")
#
# d1.add_tag("urgent")
# d1.add_tag("work")
#
# storage = Storage()
# storage.add_category(c1)
# storage.add_topic(t1)
# storage.add_document(d1)
#
# print(c1)
# print(t1)
# print(storage.get_document(1))
# print(storage)
