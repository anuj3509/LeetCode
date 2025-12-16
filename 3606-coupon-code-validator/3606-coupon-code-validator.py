class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }

        def is_valid_code(s: str) -> bool:
            if not s:
                return False
            for ch in s:
                ok = (
                    ('a' <= ch <= 'z') or
                    ('A' <= ch <= 'Z') or
                    ('0' <= ch <= '9') or
                    (ch == '_')
                )
                if not ok:
                    return False
            return True

        valid = []
        for c, b, a in zip(code, businessLine, isActive):
            if not a:
                continue
            if b not in order:
                continue
            if not is_valid_code(c):
                continue
            valid.append((order[b], c))

        valid.sort()  # (businessLine priority, then code lexicographically)
        return [c for _, c in valid]
