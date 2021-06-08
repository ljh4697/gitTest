import gym

step = 0 
score = 0

env = gym.make('MountainCar-v0')
env.reset()
while True:
    env.render()
    action = env.action_space.sample()
    obs, reward, done, info = env.step(action)
    print(score)
    score += reward
    step += 1


    if done:
        break

print('score : ', score)
print('step :', step)