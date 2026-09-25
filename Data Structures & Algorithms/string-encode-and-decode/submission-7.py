class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empt"
        encoded = ""
        for i in strs:
            encoded+=i+"spli"
        return encoded[:-4:]

    def decode(self, s: str) -> List[str]:
        if s == "empt":
            return []
        return s.split("spli")