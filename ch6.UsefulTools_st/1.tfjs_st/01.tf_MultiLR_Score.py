# Multi Linear Regression Example
import tensorflow as tf

data = [[2,0,81],[4,4,93],[6,2,91],[8,3,97]]
x1 = [x_row[0] for x_row in data]
x2 = [x_row[1] for x_row in data]
y_data = [y_row[2] for y_row in data]

learning_rate = 0.1
#learning_r!ate = 0.01   # 학습률이 작으면 epoch 을 10배이상(30001) 늘려야 비숫한 오류율(RMSE)을 획득함
a1 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
a2 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed=0))

y = a1*x1 + a2*x2 + b
rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())    
    for step in range(4001):        
        sess.run(gradient_decent)
        if step % 100 == 0:
            print("Epoch_%4d -> RMSE=%.4f, 기울기1(a1)=%.4f, 기울기2(a2)=%.4f, 절편(b)=%.4f"
                  % (step, sess.run(rmse), sess.run(a1), sess.run(a2), sess.run(b)))

    print('Predict Score => ')
    test_x1 = [2, 3, 5]
    test_x2 = [3, 4, 1]
    test_y = a1*test_x1 + a2*test_x2 + b
    print(sess.run(test_y))	

    sess.close()

#%%
    # Multi Linear Regression Example
import tensorflow as tf

data = [[2,0,81],[4,4,93],[6,2,91],[8,3,97]]
t_x1 = [x_row[0] for x_row in data]
t_x2 = [x_row[1] for x_row in data]
y_data = [y_row[2] for y_row in data]

x1 = tf.placeholder(dtype=tf.float64)
x2 = tf.placeholder(dtype=tf.float64)

learning_rate = 0.1
#learning_r!ate = 0.01   # 학습률이 작으면 epoch 을 10배이상(30001) 늘려야 비숫한 오류율(RMSE)을 획득함
a1 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
a2 = tf.Variable(tf.random_uniform([1], 0, 10, dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], 0, 100, dtype=tf.float64, seed=0))

y = a1*x1 + a2*x2 + b
rmse = tf.sqrt(tf.reduce_mean(tf.square(y - y_data)))
gradient_decent = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())    
    for step in range(4001):        
        sess.run(gradient_decent, {x1:t_x1, x2:t_x2})
        if step % 100 == 0:
            print("Epoch_%4d -> RMSE=%.4f, 기울기1(a1)=%.4f, 기울기2(a2)=%.4f, 절편(b)=%.4f"
                  % (step, sess.run(rmse, {x1:t_x1, x2:t_x2}), sess.run(a1), sess.run(a2), sess.run(b)))

    print('Predict Score => ')
    test_x1 = [2, 3, 5]
    test_x2 = [3, 4, 1]
    print(sess.run(y, {x1:test_x1, x2:test_x2}))	

    sess.close()





