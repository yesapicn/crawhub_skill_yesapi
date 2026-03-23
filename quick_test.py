#!/usr/bin/env python3
"""
快速测试 YesApi 客户端修复
"""

import sys
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_imports():
    """测试导入"""
    print("=== 测试导入 ===")
    try:
        from yesapi_client import YesApiClient, YesApiConfig, YesApiError
        print("✅ yesapi_client 导入成功")
        
        from skill_handler import YesApiSkillHandler, process_request
        print("✅ skill_handler 导入成功")
        
        return True
    except Exception as e:
        print(f"❌ 导入失败: {e}")
        return False

def test_client_init():
    """测试客户端初始化"""
    print("\n=== 测试客户端初始化 ===")
    try:
        from yesapi_client import YesApiClient
        
        client = YesApiClient()
        print("✅ 客户端初始化成功")
        print(f"配置: app_key={client.config.app_key[:10]}..., domain={client.config.domain}")
        return client
    except Exception as e:
        print(f"❌ 客户端初始化失败: {e}")
        return None

def test_skill_handler():
    """测试技能处理器"""
    print("\n=== 测试技能处理器 ===")
    try:
        from skill_handler import YesApiSkillHandler
        
        handler = YesApiSkillHandler()
        print("✅ 技能处理器初始化成功")
        
        # 测试自然语言解析
        test_requests = [
            "获取我的表单模型列表",
            "创建新表单",
            "添加字段",
            "查询用户表的数据"
        ]
        
        for req in test_requests:
            parsed = handler.parse_natural_request(req)
            print(f"请求: {req}")
            print(f"解析: {parsed}")
        
        return True
    except Exception as e:
        print(f"❌ 技能处理器测试失败: {e}")
        return False

def main():
    print("YesApi 快速测试")
    print("=" * 40)
    
    # 测试导入
    if not test_imports():
        sys.exit(1)
    
    # 测试客户端初始化
    client = test_client_init()
    if not client:
        sys.exit(1)
    
    # 测试技能处理器
    if not test_skill_handler():
        sys.exit(1)
    
    print("\n✅ 所有测试通过！")
    print("\n下一步:")
    print("1. 确保环境变量配置正确")
    print("2. 运行 python3 test_yesapi.py 进行完整测试")
    print("3. 使用 clawhub publish 发布技能")

if __name__ == "__main__":
    main()
