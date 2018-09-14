# 广度优先算法：
#
# （1）顶点v入队列。
# （2）当队列非空时则继续执行，否则算法结束。
# （3）出队列取得队头顶点v；访问顶点v并标记顶点v已被访问。
# （4）查找顶点v的第一个邻接顶点col。
# （5）若v的邻接顶点col未被访问过的，则col入队列。
# （6）继续查找顶点v的另一个新的邻接顶点col，转到步骤（5）。直到顶点v的所有未被访问过的邻接点处理完。转到步骤（2）。