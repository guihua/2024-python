async def main(args: Args) -> Output:
    params = args.params

    # 获取 'input' 字段的内容，应该是一个包含文本数据的列表
    data_list = params.get('input', [])

    # 确保 data_list 是一个列表
    if not isinstance(data_list, list):
        return {"$error": "Expected 'input' to be a list."}

    # 确保 data_list 至少有 1 个元素（假设我们只需要处理第一个元素）
    if len(data_list) < 1:
        return {"$error": "Expected at least 1 text entry in 'input'."}

    # 创建一个数组来存储提取的文本内容
    extracted_values = []

    for i, text_entry in enumerate(data_list[:1]):  # 只处理第一个元素，如果有多个元素可以修改
        # 提取 page_1 到 page_10 的内容
        for i in range(1, 11):  # 只提取 page_1 到 page_10
            page_key = f"page_{i}"

            if page_key in text_entry and text_entry[page_key].strip():  # 检查是否有非空内容
                extracted_values.append(text_entry[page_key])

    # 返回一个包含字符串内容的数组
    return {"input": extracted_values}