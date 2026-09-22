def test_login_page_check():
    """模拟校验登录页面逻辑（不启动真实浏览器）"""
    # 假设这是页面上的元素
    page_title = "The Internet"
    expected_title = "The Internet"
    # 校验标题是否一致
    assert page_title == expected_title