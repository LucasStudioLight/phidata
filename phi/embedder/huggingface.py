from typing import Dict, List, Optional, Tuple, Any
from phi.embedder.base import Embedder

from phi.utils.log import logger

try:
    from huggingface_hub import InferenceClient, SentenceSimilarityInput
except ImportError:
    raise ImportError("`huggingface-hub` not installed, please run `pip install huggingface-hub`")


class HuggingfaceCustomEmbedder(Embedder):
    """Huggingface Custom Embedder"""

    model: str = "jinaai/jina-embeddings-v2-base-code"
    api_key: Optional[str] = None
    client_params: Optional[Dict[str, Any]] = None
    huggingface_client: Optional[InferenceClient] = None

    @property
    def client(self) -> InferenceClient:
        if self.huggingface_client:
            return self.huggingface_client
        _client_params: Dict[str, Any] = {}
        if self.api_key:
            _client_params["api_key"] = self.api_key
        if self.client_params:
            _client_params.update(self.client_params)
        print(_client_params)
        return InferenceClient(**_client_params)

    def _response(self, text: str):
        _request_params: SentenceSimilarityInput = {
            "json": {"inputs": text},
            "model": self.model,
        }
        print(_request_params)
        return self.client.post(**_request_params)

    def get_embedding(self, text: str) -> List[float]:
        response = self._response(text=text)
        try:
            return response
        except Exception as e:
            logger.warning(e)
            return []

    def get_embedding_and_usage(self, text: str) -> Tuple[List[float], Dict | None]:
        return super().get_embedding_and_usage(text)