# 发布检查表

- [ ] 目标 commit/tag 已确认
- [ ] 版本号正确
- [ ] CHANGELOG / release notes 已更新
- [ ] 测试通过
- [ ] 类型检查通过（若启用）
- [ ] lint / format 通过（若启用）
- [ ] 从干净环境重建
- [ ] 构建 wheel / sdist
- [ ] 检查构建产物没有 secret、临时文件、内部测试数据
- [ ] 新虚拟环境安装 wheel
- [ ] CLI / 服务启动 smoke test
- [ ] 配置/数据迁移已验证
- [ ] 发布凭据安全注入
- [ ] 发布后验证版本和核心功能
- [ ] 明确回滚方案
