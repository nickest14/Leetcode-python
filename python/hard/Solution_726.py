# 726. Number of Atoms


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n: int = len(formula)
        result_counter: dict[str, str] = {}
        parenthesis_stack: list[dict[str, int]] = []
        cur_ind = 0

        while cur_ind < n:
            cur_char: str = formula[cur_ind]
            if cur_char == "(":
                cur_ind += 1
                parenthesis_stack.append({})

            elif cur_char == ")":
                mult: str = ''
                cur_ind += 1
                while cur_ind < n and formula[cur_ind].isdigit():
                    mult += formula[cur_ind]
                    cur_ind += 1
                last_counter: dict[str, int] = parenthesis_stack.pop()
                target: dict[str, int] = parenthesis_stack[-1] if parenthesis_stack else result_counter
                for elem, counter in last_counter.items():
                    if elem not in target:
                        target[elem] = 0
                    target[elem] += counter * (int(mult) if mult else 1)

            else:
                cur_elem: str = ''
                cur_counter: str = ''
                target: dict[str, int] = parenthesis_stack[-1] if parenthesis_stack else result_counter
                while cur_ind < n and cur_char not in '()':
                    if cur_char.isalpha():
                        if cur_char.isupper() and cur_elem != '':
                            if cur_elem not in target:
                                target[cur_elem] = 0
                            target[cur_elem] += int(cur_counter) if cur_counter else 1
                            cur_counter = ''
                            cur_elem = ''
                        cur_elem += cur_char
                    else:
                        cur_counter += cur_char

                    cur_ind += 1
                    if cur_ind != n:
                        cur_char = formula[cur_ind]
                target = parenthesis_stack[-1] if parenthesis_stack else result_counter
                if cur_elem not in target:
                    target[cur_elem] = 0
                target[cur_elem] += int(cur_counter) if cur_counter else 1

        parts: list[str] = [
            elem + str(counter) if not counter == 1 else elem for elem, counter in result_counter.items()
        ]
        parts.sort()

        return ''.join(parts)


ans = Solution().countOfAtoms("K4(ON(SO3)2)2")
# ans = Solution().countOfAtoms("K4(MgON(SO3)2)2")
print(ans)
