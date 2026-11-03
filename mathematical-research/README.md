# mathematical-research — 个人数学研究 Skill

这是按研究目标设计的通用数学研究 Skill。核心规范写在 `SKILL.md`；其他参考文件只在遇到对应问题时按需读取，以减少文献综述与流程描述对研究资源的占用。

## 文件

- `SKILL.md`：必须文件；问题忠实性、简洁文献调查、候选路线生成与双重排序、深入研究、坚持性、严格审查、最终报告与续接记录。
- `references/literature-review.md`：分层文献阅读、证明方法提取、定向检索和文献可靠性。
- `references/proof-protocol.md`：决定性瓶颈的证明、失败修复、路线状态和审查。
- `references/construction.md`：存在性与显式构造核查；包含按需使用的代数曲面/双覆盖检查项。
- `references/computation.md`：计算实验、有限域、精确性与可复现性。
- `references/writing.md`：英文 LaTeX 论文式报告和未解决时自动生成的续接记录。
- `assets/research-report-template.tex`：可选的 TeX 报告框架（需替换占位内容并移除不适用章节）。

## 使用

将完整的 `mathematical-research/` 文件夹放入支持 Agent Skills 的客户端所指定的 Skill 位置，或在相应产品中导入该文件夹（不同客户端的安装步骤可能不同）。仅在平台成功加载 Skill 后，其规则才能自动触发；上传文件并不等于已经启用。

可以这样发起任务：

> 请使用 mathematical-research Skill，研究以下数学存在性问题。保持原问题的底域与全部假设；先做必要的定向文献检索，生成并排序候选路线，然后自主深入研究。最终输出英文 LaTeX 论文式报告；若尚未完整解决，自动附 Research Continuation Record。研究问题：……

## 特别提醒

该 Skill 不承诺解决所有开放问题，也不能直接改变模型的内部计算预算。它通过减少不必要的文献深读、工作日志和重复路线讨论，把可用资源尽量引导到数学证明与构造。默认通用；代数曲面只是按需示例，并非强行限制研究领域。
