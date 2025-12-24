from multi_doc_chat.custom_logger import CustomLogger
from multi_doc_chat.custom_exception import DocumentPortalException

#**************************************************** RUN 1 *********************************#
# if __name__ == "__main__":
#     logger_manager = CustomLogger()
#     logger = logger_manager.get_logger(__file__)
#     print("****************************",logger ,"*************", __file__)

#     logger.info("Application started")


# def divide_numbers(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         # Wrap original exception
#         raise DocumentPortalException(
#             "Failed while dividing numbers",
#             e
#         )

# if __name__ == "__main__":
#     divide_numbers(10, 0)

#**************************************************** RUN 2 *********************************#

# def divide(a, b):
#     try:
#         return a / b
#     except Exception as e:
#         # Wrap low-level exception
#         raise DocumentPortalException("Division operation failed", e)


# if __name__ == "__main__":
#     logger_manager = CustomLogger()
#     logger = logger_manager.get_logger(__file__)

#     try:
#         divide(10, 0)
#     except DocumentPortalException as e:
#         # Log structured error
#         logger.error(
#             "Application error occurred",
#             error=str(e),   # kinda calling function from here
#             file=e.file_name,
#             line=e.line_no,
#         )

#**************************************************** RUN 3_YAML and loding YAML and loading it using Configloader *********************************#
# from multi_doc_chat.config_loader import load_config
# from pprint import pprint

# def main():
#     path = "multi_doc_chat\config.yaml"
#     config = load_config(path=path)

#     print("\n--- FULL CONFIG ---")
#     pprint(config)

#     embedding_cfg = config["embedding_model"]
#     retriever_cfg = config["retriever"]
#     llm_cfg = config["llm"]["mistral"]  # switch to ["google"] if needed

#     print("\n--- EMBEDDING CONFIG ---")
#     pprint(embedding_cfg)

#     print("\n--- RETRIEVER CONFIG ---")
#     pprint(retriever_cfg)

#     print("\n--- LLM CONFIG ---")
#     pprint(llm_cfg)


# if __name__ == "__main__":
#     main()

#**************************************************** RUN 4_ Let's first load the documents from data folder*********************************#

from pathlib import Path
from multi_doc_chat.load_documents import load_documents_from_folder


def main():
    data_folder = Path("data")   # 👈 your data folder
    docs = load_documents_from_folder(data_folder)

    print(f"\nTotal documents loaded: {len(docs)}")

    if docs:
        print("\nSample document content:")
        print(docs[0].page_content[:500])


if __name__ == "__main__":
    main()



