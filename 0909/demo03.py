async def main(args: Args) -> Output:
    params = args.params

    data_list = params.get('input', [])

    if not isinstance(data_list, list):
        return {"$error": "Expected 'input' to be a list."}

    # 检查列表元素是否都是字符串
    if not all(isinstance(item, str) for item in data_list):
        return {"$error": "Expected all items in 'input' to be strings."}

    # 直接返回字符串列表
    return {"input": data_list}