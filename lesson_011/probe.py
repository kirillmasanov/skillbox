def log_errors_file(file_name):
    def log_errors(func):
        def surrogate(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except BaseException as exc:
                # print(f'Какая то еще ошибка: "{exc}"')
                with open(file_name, 'a', encoding='utf-8') as ff:
                    ff.write(f'<{func.__name__}> <{args},{kwargs}> <{exc}> <{exc.args}>\n')
                raise

        return surrogate

    return log_errors


@log_errors_file('aaa.txt')
def perky(param):
    return param / 0


perky(param=42)
