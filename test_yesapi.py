"""
YesApi Skill 测试文件
用于验证功能和本地调试
"""

import os
import sys
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_configuration():
    """测试配置"""
    print("=== 测试配置 ===")
    
    app_key = os.getenv("YESAPI_APP_KEY")
    domain = os.getenv("YESAPI_DOMAIN", "https://api.yesapi.net")
    sign = os.getenv("YESAPI_SIGN")
    
    print(f"App Key: {'已配置' if app_key else '❌ 未配置'}")
    print(f"Domain: {domain}")
    print(f"Sign: {'已配置' if sign else '❌ 未配置'}")
    
    if not app_key:
        print("\n❌ 请在 .env 文件中配置 YESAPI_APP_KEY")
        return False
    
    return True

def test_client_initialization():
    """测试客户端初始化"""
    print("\n=== 测试客户端初始化 ===")
    
    try:
        from yesapi_client import YesApiClient, YesApiConfig
        
        config = YesApiConfig(
            app_key=os.getenv("YESAPI_APP_KEY", ""),
            domain=os.getenv("YESAPI_DOMAIN", "https://api.yesapi.net"),
            sign=os.getenv("YESAPI_SIGN", "")
        )
        
        client = YesApiClient(config)
        print("✅ 客户端初始化成功")
        return client
        
    except Exception as e:
        print(f"❌ 客户端初始化失败: {e}")
        return None

def test_api_connection(client):
    """测试API连接"""
    print("\n=== 测试API连接 ===")
    
    try:
        # 测试获取模型列表
        result = client.get_models()
        print("✅ API连接成功")
        print(f"返回数据: {result}")
        return True
        
    except YesApiError as e:
        print(f"❌ API错误: {e}, ret: {e.ret}")
        return False
    except Exception as e:
        print(f"❌ API连接失败: {e}")
        return False

def test_skill_handler():
    """测试Skill处理器"""
    print("\n=== 测试Skill处理器 ===")
    
    try:
        from skill_handler import YesApiSkillHandler, process_request
        
        handler = YesApiSkillHandler()
        
        # 测试自然语言解析
        test_requests = [
            "获取我的表单模型列表",
            "查询用户表的数据",
            "向订单表添加新数据"
        ]
        
        for req in test_requests:
            parsed = handler.parse_natural_request(req)
            print(f"请求: {req}")
            print(f"解析: {parsed}")
        
        print("✅ Skill处理器测试成功")
        return True
        
    except Exception as e:
        print(f"❌ Skill处理器测试失败: {e}")
        return False

def interactive_test():
    """交互式测试"""
    print("\n=== 交互式测试 ===")
    print("输入 'quit' 退出测试")
    
    try:
        from skill_handler import process_request
        
        while True:
            request = input("\n请输入测试请求: ").strip()
            if request.lower() == 'quit':
                break
            
            params = {}
            
            # 如果请求包含表名，尝试提取
            if "表" in request:
                # 简单的表名提取逻辑
                import re
                table_match = re.search(r'(\w+)表', request)
                if table_match:
                    params['model_name'] = table_match.group(1)
            
            result = process_request(request, params)
            print(f"结果: {result}")
            
    except KeyboardInterrupt:
        print("\n测试结束")
    except Exception as e:
        print(f"❌ 交互式测试失败: {e}")

def main():
    """主测试函数"""
    print("YesApi Skill 本地测试")
    print("=" * 50)
    
    # 1. 测试配置
    if not test_configuration():
        return
    
    # 2. 测试客户端初始化
    client = test_client_initialization()
    if not client:
        return
    
    # 3. 测试API连接（可选，需要有效的API密钥）
    if os.getenv("YESAPI_APP_KEY"):
        test_api_connection(client)
    else:
        print("\n⚠️  跳过API连接测试（未配置有效的API密钥）")
    
    print("\n测试完成！")

if __name__ == "__main__":
    main()
