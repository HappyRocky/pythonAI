# -*- coding: utf-8 -*-

import xgboost as xgb
from sklearn.metrics import accuracy_score
import time
def train(train_file, test_file):
    '''
    读取训练数据，并用xgboost训练
    '''
    dtrain = xgb.DMatrix(train_file)
    dtest = xgb.DMatrix(test_file)
    print(f'训练集大小：{dtrain.num_row()}*{dtrain.num_col()}, 测试集大小：{dtest.num_row()}*{dtest.num_col()}')
    
    
    #设置参数：
    param = {
            'booster': 'gbtree',
            'objective': 'binary:logistic',  # “binary:logistic” 表示二分类的逻辑回归问题，输出为概率。多分类的问题可以使用'multi:softmax'
            #'num_class': 3,               # 类别数，与 multisoftmax 并用，二分类时不要加这个参数
            'gamma': 2,                  # 用于控制是否后剪枝的参数,越大越保守，一般0.1、0.2这样子。
            'max_depth': 8,               # 构建树的深度，越大越容易过拟合。缺省值为6，取值范围为：[1,∞]。
            'lambda': 1,                   # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
            'subsample': 0.8,              # 随机采样训练样本
            'colsample_bytree': 0.8,       # 生成树时进行的列采样
            'min_child_weight': 3,
            'silent': 0,                   # 设置成1则没有运行信息输出，最好是设置为0。缺省值为0。
            'eta': 0.3,                  # 为了防止过拟合，更新过程中用到的收缩步长，如同学习率。缺省值为0.3，取值范围为：[0,1]。
            'seed': 1000,
            'nthread': 4,                  # cpu 线程数
            }
    
    # 训练模型
    num_round = 2
    start_time = time.clock()
    bst = xgb.train(param, dtrain, num_round) # 训练
    endtime = time.clock()
    print(f'运行时间:{endtime - start_time}')
    
    # 训练集正确率
    train_preds = bst.predict(dtrain)
    train_predictions = [round(value) for value in train_preds]
    y_train = dtrain.get_label()
    train_accuracy = accuracy_score(y_train, train_predictions)
    print(f'训练集正确率：{train_accuracy}')
    
    # 测试集正确率
    test_preds = bst.predict(dtest)
    test_predictions = [round(value) for value in test_preds]
    y_test = dtest.get_label()
    test_accuracy = accuracy_score(y_test, test_predictions)
    print(f'测试集正确率：{test_accuracy}')    
    
    # 可视化
    from matplotlib import pyplot
    import graphviz
    #xgb.plot_tree(bst, num_trees=0, rankdir= 'LR' )
    #pyplot.show()
 
    #xgb.plot_tree(bst,num_trees=1, rankdir= 'LR' )
    #pyplot.show()
    #xgb.to_graphviz(bst,num_trees=0)
    #xgb.to_graphviz(bst,num_trees=1)

    
if '__main__' == __name__:
    train_file = 'data/a5a_train.data'
    test_file = 'data/a5a_test.data'
    train(train_file, test_file)