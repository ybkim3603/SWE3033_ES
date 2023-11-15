from elasticsearch import Elasticsearch, helpers
from src.configuration import Configuration


class ElasticsearchClient:
    def __init__(self):
        self.config = Configuration().get_config('elasticsearch')
        self.client = self.connect_to_elastic()

    def connect_to_elastic(self) -> Elasticsearch:
        client = Elasticsearch(
            f"{self.config['host']}:{self.config['port']}",
            ca_certs=self.config['ca_cert'],
            basic_auth=(self.config['username'], self.config['password'])
        )
        return client
        
    def create_index(self, index_name: str, mapping: dict) -> None:
        ################# EDIT HERE #################
        pass



        ################# EDIT HERE #################

    def insert_one_document(self, index_name:str, body: dict, doc_id=None) -> None:
        ################# EDIT HERE #################
        response = None
        ################# EDIT HERE #################

    def get_document(self, index_name: str, doc_id: int) -> dict:
        ################# EDIT HERE #################
        response = None
        ################# EDIT HERE #################
        return response['_source']
    
    def update_document_by_id(self, index_name: str, doc_id: int, body: dict) -> None:
        ################# EDIT HERE #################
        response = None
        ################# EDIT HERE #################

    def delete_index(self, index_name: str) -> None:
        ################# EDIT HERE #################
        pass
        ################# EDIT HERE #################
    
    def delete_document(self, index_name: str, doc_id: int) -> None:
        ################# EDIT HERE #################
        response = None
        ################# EDIT HERE #################

    def search(self, query: dict, index_name: str) -> list:
        ################# EDIT HERE #################
        result = None



        ################# EDIT HERE #################
        return result['hits']['hits']
    
    def count(self, index_name: str) -> int:
        self.client.indices.refresh(index=index_name)
        ################# EDIT HERE #################
        result = 0
        ################# EDIT HERE #################
        return result['count']
    
    def scan_index(self, index_name: str, query: dict, size: int, scroll='2m') -> list:
        ################# EDIT HERE #################
        response = None
        ################# EDIT HERE #################
        for doc in response:
            yield doc['_source']
    
    def bulk_request(self, actions: list = None) -> None:
        ################# EDIT HERE #################
        pass
        ################# EDIT HERE #################
