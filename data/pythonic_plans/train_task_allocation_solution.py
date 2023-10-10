# EXAMPLE 1 - Task Description: Turn off the light and turn on the faucet. 
# GENERAL TASK DECOMPOSITION
# Independent subtasks:
# SubTask 1: Turn off the light. (Skills Required: GoToObject, SwitchOff)
# SubTask 2: Turn on the faucet. (Skills Required: GoToObject, SwitchOff)
# We can perform SubTask 1 and SubTask 2 in parallel.

# CODE
def turn_off_light():
    # 0: SubTask 1: Turn off the light
    # 1: Go to the LightSwitch.
    GoToObject('LightSwitch')
    # 2: Switch off the LightSwitch.
    SwitchOff('LightSwitch')
def turn_on_faucet():
    # 0: SubTask 1: Turn on the faucet
    # 1: Go to the Faucet.
    GoToObject('Faucet')
    # 2: Switch on the Faucet.
    SwitchOn('Faucet')
# Perform SubTask 1 and SubTask 2 in parallel
task1_thread = threading.Thread(target=turn_off_light)
task2_thread = threading.Thread(target=turn_on_faucet)
# Start executing SubTask 1 and SubTask 2
task1_thread.start()
task2_thread.start()
# Task turn off the light is done

# TASK ALLOCATION
# Scenario: There are 2 robots available. The task should be performed using the minimum number of robots necessary. Robots should be assigned to subtasks that match its skills and mass capacity. 
# Task Allocation Rules: Each subtask should be assigned to a robot or a team of robots that collectively possess all the skills required for the subtask and can handle the mass of the objects involved in the task. If a subtask cannot be performed by a single robot due to its skill set or mass capacity, form a team of robots to perform the subtask. The combined skills and mass capacity of the team should meet all the skill and mass requirements of the subtask. If a subtask can be performed in parallel with other subtasks (i.e., it does not depend on the completion of other tasks), assign it to a robot or team that can start immediately and can handle the mass of the objects involved. If a subtask must be performed sequentially after other subtasks (i.e., it depends on the completion of other subtasks), assign it to a robot or team that can start as soon as the preceding subtasks are complete and can handle the mass of the objects involved. Based on the 'GENERAL TASK DECOMPOSITION' given above, identify the subtasks for each main task, the skills required for each subtask, and the mass of the objects and mass capacity of robots involved in each subtask. Determine whether the subtasks must be performed sequentially or in parallel, or a combination of both, and whether the mass of the objects involved in the subtasks is within the mass capacity of the robots or teams.
robots = [{'name': 'robot1', 'no_skills': 9, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'],'mass': 2}, {'name': 'robot2', 'no_skills': 13, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'PickupObject', 'PutObject', 'SwitchOn', 'SwitchOff', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'],'mass': 2}]
objects = [{'name': 'SaltShaker', 'mass': 1.0}, {'name': 'SoapBottle', 'mass': 5.0}, {'name': 'Bowl', 'mass': 3.0}, {'name': 'CounterTop', 'mass': 2}, {'name': 'Drawer', 'mass': 5}, {'name': 'Vase', 'mass': 1}, {'name': 'Lettuce', 'mass': 5}, {'name': 'Plate', 'mass': 5}, {'name': 'Potato', 'mass': 2}, {'name': 'Pan', 'mass': 5}, {'name': 'Window', 'mass': 4}, {'name': 'Fridge', 'mass': 4}, {'name': 'Sink', 'mass': 5}, {'name': 'Stool', 'mass': 6}, {'name': 'DiningTable', 'mass': 6}, {'name': 'HousePlant', 'mass': 2}, {'name': 'Chair', 'mass': 6}, {'name': 'Cup', 'mass': 3}, {'name': 'Shelf', 'mass': 6}, {'name': 'StoveKnob', 'mass': 3}, {'name': 'ButterKnife', 'mass': 6}, {'name': 'Bread', 'mass': 2}, {'name': 'DishSponge', 'mass': 4}, {'name': 'Floor', 'mass': 4}, {'name': 'PepperShaker', 'mass': 2}, {'name': 'Spatula', 'mass': 2}, {'name': 'StoveBurner', 'mass': 4}, {'name': 'Statue', 'mass': 1}, {'name': 'Kettle', 'mass': 2}, {'name': 'Apple', 'mass': 4}, {'name': 'WineBottle', 'mass': 5}, {'name': 'Knife', 'mass': 6}, {'name': 'GarbageCan', 'mass': 5}, {'name': 'Microwave', 'mass': 5}, {'name': 'LightSwitch', 'mass': 6}, {'name': 'Pot', 'mass': 2}, {'name': 'Egg', 'mass': 3}, {'name': 'Mug', 'mass': 2}, {'name': 'CoffeeMachine', 'mass': 6}, {'name': 'Faucet', 'mass': 6}, {'name': 'Tomato', 'mass': 4}, {'name': 'Spoon', 'mass': 2}, {'name': 'Fork', 'mass': 4.8}, {'name': 'Toaster', 'mass': 1}, {'name': 'Book', 'mass': 6}, {'name': 'SinkBasin', 'mass': 6}, {'name': 'Cabinet', 'mass': 1}, {'name': 'ShelvingUnit', 'mass': 3}]

# SOLUTION
# Robot 1 has 9 skills, while Robot 2 has 13 skills. Robots do not have same number of skills. 
# All the robots DONOT share the same set and number of skills (no_skills) and objects have different mass. In this case where all robots have different sets of skills and objects have different mass - Focus on Task Allocation based on Robot Skills alone. 
# Analyze the skills required for each subtask and the skills each robot possesses. In this scenario, we have one subtask: 'Turn off the light'.
# For the 'Turn off the light' subtask, it can be performed by any robot with 'GoToObject' and 'SwitchOff' skills. In this case, Robots 2 has all these skills.
# For the 'Turn on the faucet' subtask, it can be performed by any robot with 'GoToObject' and 'SwitchOff' skills. In this case, Robots 2 has all these skills.
# No teams are required since SubTasks can be performed with individual robots as explained above. The 'Turn off the light' and 'Turn on the faucet' subtasks are assigned to Robot 2. 
# Robot 2 cannot do both the SubTasks in parallel. Serialize the SubTasks and perform them one after the other using Robot 2. 



# EXAMPLE 2 - Task Description: Slice the Potato 
# GENERAL TASK DECOMPOSITION
# Independent subtasks:
# SubTask 1: Slice the Potato. (Skills Required: GoToObject, PickupObject, SliceObject, PutObject)
# We can execute SubTask 1 first.

# CODE
def slice_potato():
    # 0: SubTask 1: Slice the Potato
    # 1: Go to the Knife.
    GoToObject('Knife')
    # 2: Pick up the Knife.
    PickupObject('Knife')
    # 3: Go to the Potato.
    GoToObject('Potato')
    # 4: Slice the Potato.
    SliceObject('Potato')
    # 5: Go to the countertop.
    GoToObject('CounterTop')
    # 6: Put the Knife back on the CounterTop.
    PutObject('Knife', 'CounterTop')
# Execute SubTask 1
slice_potato()
# Task fry sliced potato is done


# TASK ALLOCATION
# Scenario: There are 3 robots available. The task should be performed using the minimum number of robots necessary. Robots should be assigned to subtasks that match its skills and mass capacity. 
# Task Allocation Rules: Each subtask should be assigned to a robot or a team of robots that collectively possess all the skills required for the subtask and can handle the mass of the objects involved in the task. If a subtask cannot be performed by a single robot due to its skill set or mass capacity, form a team of robots to perform the subtask. The combined skills and mass capacity of the team should meet all the skill and mass requirements of the subtask. If a subtask can be performed in parallel with other subtasks (i.e., it does not depend on the completion of other tasks), assign it to a robot or team that can start immediately and can handle the mass of the objects involved. If a subtask must be performed sequentially after other subtasks (i.e., it depends on the completion of other subtasks), assign it to a robot or team that can start as soon as the preceding subtasks are complete and can handle the mass of the objects involved. Based on the 'GENERAL TASK DECOMPOSITION' given above, identify the subtasks for each main task, the skills required for each subtask, and the mass of the objects and mass capacity of robots involved in each subtask. Determine whether the subtasks must be performed sequentially or in parallel, or a combination of both, and whether the mass of the objects involved in the subtasks is within the mass capacity of the robots or teams.
robots = [{'name': 'robot1', 'no_skills': 5, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject'],'mass': 2}, {'name': 'robot2', 'no_skills': 10, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SwitchOn', 'SwitchOff', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'],'mass': 2}, {'name': 'robot3', 'no_skills': 7, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'PickupObject', 'PutObject', 'DropHandObject'],'mass': 2}]
objects = [{'name': 'SaltShaker', 'mass': 1.0}, {'name': 'SoapBottle', 'mass': 5.0}, {'name': 'Bowl', 'mass': 3.0}, {'name': 'CounterTop', 'mass': 2}, {'name': 'Drawer', 'mass': 5}, {'name': 'Vase', 'mass': 1}, {'name': 'Lettuce', 'mass': 5}, {'name': 'Plate', 'mass': 5}, {'name': 'Potato', 'mass': 2}, {'name': 'Pan', 'mass': 5}, {'name': 'Window', 'mass': 4}, {'name': 'Fridge', 'mass': 4}, {'name': 'Sink', 'mass': 5}, {'name': 'Stool', 'mass': 6}, {'name': 'DiningTable', 'mass': 6}, {'name': 'HousePlant', 'mass': 2}, {'name': 'Chair', 'mass': 6}, {'name': 'Cup', 'mass': 3}, {'name': 'Shelf', 'mass': 6}, {'name': 'StoveKnob', 'mass': 3}, {'name': 'ButterKnife', 'mass': 6}, {'name': 'Bread', 'mass': 2}, {'name': 'DishSponge', 'mass': 4}, {'name': 'Floor', 'mass': 4}, {'name': 'PepperShaker', 'mass': 2}, {'name': 'Spatula', 'mass': 2}, {'name': 'StoveBurner', 'mass': 4}, {'name': 'Statue', 'mass': 1}, {'name': 'Kettle', 'mass': 2}, {'name': 'Apple', 'mass': 4}, {'name': 'WineBottle', 'mass': 5}, {'name': 'Knife', 'mass': 6}, {'name': 'GarbageCan', 'mass': 5}, {'name': 'Microwave', 'mass': 5}, {'name': 'LightSwitch', 'mass': 6}, {'name': 'Pot', 'mass': 2}, {'name': 'Egg', 'mass': 3}, {'name': 'Mug', 'mass': 2}, {'name': 'CoffeeMachine', 'mass': 6}, {'name': 'Faucet', 'mass': 6}, {'name': 'Tomato', 'mass': 4}, {'name': 'Spoon', 'mass': 2}, {'name': 'Fork', 'mass': 4.8}, {'name': 'Toaster', 'mass': 1}, {'name': 'Book', 'mass': 6}, {'name': 'SinkBasin', 'mass': 6}, {'name': 'Cabinet', 'mass': 1}, {'name': 'ShelvingUnit', 'mass': 3}]

# SOLUTION
# Robot 1 has 5 skills, while Robot 2 has 10 and robot 3 has 7 skills. Robots do not have same number of skills.
# All the robots DONOT share the same set and number of skills (no_skills) and objects have different mass. In this case where all robots have different sets of skills and objects have different mass - Focus on Task Allocation based on Robot Skills alone. 
# Analyze the skills required for each subtask and the skills each robot possesses. In this scenario, we have one main subtasks: 'Slice the Potato'.
# For the 'Slice the Potato' subtask, it can be performed by any robot with 'GoToObject', 'PickupObject', 'SliceObject' and 'PutObject' skills. However, no individual robot has all these skills. This is a skill gap that needs to be addressed. Form a team of robots. The skills of the team must be 'GoToObject', 'PickupObject', 'SliceObject' and 'PutObject' skills. Team of Robots 1 and 3 have all the skills required where robot 1 has the 'SliceObject' skill and Robot 3 has the 'GoToObject', 'PickupObject', and 'PutObject' skills.
# Teams are required since SubTasks can't be performed with individual robots as explained above. The 'Slice the Potato' subtask is assigned to team of Robots 1 and 3. 



# EXAMPLE 3 - Task Description: Throw the fork and spoon in the trash
# GENERAL TASK DECOMPOSITION
# Independent subtasks:
# SubTask 1: Throw the Fork in the trash. (Skills Required: GoToObject, PickupObject, ThrowObject)
# SubTask 2: Throw the Spoon in the trash. (Skills Required: GoToObject, PickupObject, ThrowObject)
# We can execute SubTask 1 first and then SubTask 2.

# CODE
def throw_fork_in_trash():
    # 0: SubTask 1: Throw the Fork in the trash
    # 1: Go to the Fork.
    GoToObject('Fork')
    # 2: Pick up the Fork.
    PickupObject('Fork')
    # 3: Go to the GarbageCan.
    GoToObject('GarbageCan')
    # 4: Throw the Fork in the GarbageCan.
    ThrowObject('Fork', 'GarbageCan')
def throw_spoon_in_trash():
    # 0: SubTask 2: Throw the Spoon in the trash
    # 1: Go to the Spoon.
    GoToObject('Spoon')
    # 2: Pick up the Spoon.
    PickupObject('Spoon')
    # 3: Go to the GarbageCan.
    GoToObject('GarbageCan')
    # 4: Throw the Spoon in the GarbageCan.
    ThrowObject('Spoon', 'GarbageCan')
# Execute SubTask 1
throw_fork_in_trash()
# Execute SubTask 2
throw_spoon_in_trash()


# TASK ALLOCATION
# Scenario: There are 3 robots available. The task should be performed using the minimum number of robots necessary. Robots should be assigned to subtasks that match its skills and mass capacity. 
# Task Allocation Rules: Each subtask should be assigned to a robot or a team of robots that collectively possess all the skills required for the subtask and can handle the mass of the objects involved in the task. If a subtask cannot be performed by a single robot due to its skill set or mass capacity, form a team of robots to perform the subtask. The combined skills and mass capacity of the team should meet all the skill and mass requirements of the subtask. If a subtask can be performed in parallel with other subtasks (i.e., it does not depend on the completion of other tasks), assign it to a robot or team that can start immediately and can handle the mass of the objects involved. If a subtask must be performed sequentially after other subtasks (i.e., it depends on the completion of other subtasks), assign it to a robot or team that can start as soon as the preceding subtasks are complete and can handle the mass of the objects involved. Based on the 'GENERAL TASK DECOMPOSITION' given above, identify the subtasks for each main task, the skills required for each subtask, and the mass of the objects and mass capacity of robots involved in each subtask. Determine whether the subtasks must be performed sequentially or in parallel, or a combination of both, and whether the mass of the objects involved in the subtasks is within the mass capacity of the robots or teams.
robots = [{'name': 'robot1', 'no_skills': 13, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'PickupObject', 'PutObject', 'SwitchOn', 'SwitchOff', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'],'mass': 3.2}, {'name': 'robot2', 'no_skills': 13, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'PickupObject', 'PutObject', 'SwitchOn', 'SwitchOff', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'],'mass': 2.0}, {'name': 'robot3', 'no_skills': 13, 'skills': ['GoToObject', 'OpenObject', 'CloseObject', 'BreakObject', 'SliceObject', 'PickupObject', 'PutObject', 'SwitchOn', 'SwitchOff', 'DropHandObject', 'ThrowObject', 'PushObject', 'PullObject'],'mass': 2.0}]
objects = [{'name': 'SaltShaker', 'mass': 1.0}, {'name': 'SoapBottle', 'mass': 5.0}, {'name': 'Bowl', 'mass': 3.0}, {'name': 'CounterTop', 'mass': 2}, {'name': 'Drawer', 'mass': 5}, {'name': 'Vase', 'mass': 1}, {'name': 'Lettuce', 'mass': 5}, {'name': 'Plate', 'mass': 5}, {'name': 'Potato', 'mass': 2}, {'name': 'Pan', 'mass': 5}, {'name': 'Window', 'mass': 4}, {'name': 'Fridge', 'mass': 4}, {'name': 'Sink', 'mass': 5}, {'name': 'Stool', 'mass': 6}, {'name': 'DiningTable', 'mass': 6}, {'name': 'HousePlant', 'mass': 2}, {'name': 'Chair', 'mass': 6}, {'name': 'Cup', 'mass': 3}, {'name': 'Shelf', 'mass': 6}, {'name': 'StoveKnob', 'mass': 3}, {'name': 'ButterKnife', 'mass': 6}, {'name': 'Bread', 'mass': 2}, {'name': 'DishSponge', 'mass': 4}, {'name': 'Floor', 'mass': 4}, {'name': 'PepperShaker', 'mass': 2}, {'name': 'Spatula', 'mass': 2}, {'name': 'StoveBurner', 'mass': 4}, {'name': 'Statue', 'mass': 1}, {'name': 'Kettle', 'mass': 2}, {'name': 'Apple', 'mass': 4}, {'name': 'WineBottle', 'mass': 5}, {'name': 'Knife', 'mass': 6}, {'name': 'GarbageCan', 'mass': 5}, {'name': 'Microwave', 'mass': 5}, {'name': 'LightSwitch', 'mass': 6}, {'name': 'Pot', 'mass': 2}, {'name': 'Egg', 'mass': 3}, {'name': 'Mug', 'mass': 2}, {'name': 'CoffeeMachine', 'mass': 6}, {'name': 'Faucet', 'mass': 6}, {'name': 'Tomato', 'mass': 4}, {'name': 'Spoon', 'mass': 2.0}, {'name': 'Fork', 'mass': 4.8}, {'name': 'Toaster', 'mass': 1}, {'name': 'Book', 'mass': 6}, {'name': 'SinkBasin', 'mass': 6}, {'name': 'Cabinet', 'mass': 1}, {'name': 'ShelvingUnit', 'mass': 3}]

# SOLUTION
# Robot 1, 2 and 3 have 13 skills. All robots do have same number of skills.
# All the robots share the same set and number of skills (no_skills) & all objects DONOT have same mass. In this case where all robots have same skills and all objects have different mass- Focus on Task Allocation based on Mass alone. 
# Analyze the mass required for each object being PickedUp by the 'PickupObject' skill, and the mass capacity each robot possesses. In this scenario, we have two main subtasks: 'Throw the Fork in the trash' and 'Throw the Spoon in the trash'.
# For the 'Throw the Fork in the trash' subtask, mass of the Fork is 4.8. Hence the subtask can be performed by any robot with mass capacity greater than or equal to 4.8. However, no individual robot has mass capacity of 4.8. This is a mass gap that needs to be addressed. Form a team of robots. The combined mass capacity of the team must be greater than or equal to 4.8. Team of Robots 1 and 2 have the mass capacity required.
# For the 'Throw the Spoon in the trash' subtask, mass of the Spoon is 2.0. Hence the subtask can be performed by any robot with mass capacity greater than or equal to 2.0. In this case, Robots 3 has a mass capacity = 2.0.
# Teams are required since SubTasks can't be performed with individual robots as explained above. The 'Throw the Fork in the trash' subtask is assigned to team of Robots 1 and 2. The 'Throw the Spoon in the trash' subtask is assigned to Robots 3. 