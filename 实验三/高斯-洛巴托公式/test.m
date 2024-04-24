% 计算积分
q1 = IntGaussLobato('exp(-x)*sin(x)', 0, 10, 4, 0, 0);
q2 = IntGaussLobato('exp(-x)*sin(x)', 0, 10, 5, 0, 0);
q3 = IntGaussLobato('exp(-x)*sin(x)', 0, 10, 6, 0, 0);


% 将 sym 计算成数值
eval_q1 = eval(q1);
eval_q2 = eval(q2);
eval_q3 = eval(q3);

% 显示结果
disp(['n=4时，积分结果为：', num2str(eval_q1)]);
disp(['n=5时，积分结果为：', num2str(eval_q2)]);
disp(['n=6时，积分结果为：', num2str(eval_q3)]);