import random
choices = ["A","B"]
choices2a = random.choice(choices)
print(choices2a)

from time import sleep 
print("We will first ask for your name and introduce you to our story.")
name = raw_input("what is your name? ")
print "Hi "+ name + (" Welcome to our story called Muerte.") 
print("You are able to make choices with either 'A','a', or 'B',and 'b'.")
sleep(1)
print("This story deals with two perspectives, Jeff's or Verne's. This story takes place at a party.")
sleep(1)
print("Choice A: Jeff")
print("Choice B: Verne")
choice1 = raw_input("Choose Jeff or Verne?:")
if choice1 == "a" or choice1 == "A":
    print("Your are Jeff, a college student who studies at Pug University, but the twist is he's a murderer.")
    print("Jeff was invited to the party.")
    sleep(2)
    print("You have a choice to go or not.")
    print("Choice A: You go")
    print("choice B: You dont go")
    choice2a = raw_input("You go or dont go?: ")
    if choice2a == "a" or choice2a == "A":
        print("You go and hangout with your friends and you are up to no good.")
        print("Jeff drinks a few, and wonders who he will take the pleasure in killing")
        sleep(2)
        print("Jeff's friend Edward tells him that Kat, Verne's best friend, seems to like him because she been staring at him the entire night.")
        print("Jeff seems to be interested in Kat as well. He wonders if he should go talk to her.")
        print("Choice A:Talk to Kat.")
        print("Choice B: Don't talk to her.")
        choice5a = raw_input("Talk to her or not?")
        if choice5a == "a" or choice5a == "A":
            print("Jeff approaches Kat and begins to talk to her. Kat seems to be disgusted that he's been drinking. She leaves the conversation and this angers Jeff.")
        print("Doesn't know if he should follow her or not.")
        print("Choice A: Doesnt follow her.")
        print("Choice B: Follows Kat.")
        choice6a = raw_input("Follows her or not")
        if choice6a == "a" or choice6a == "A":
            print("Leaves party and goes to a theater and watches Star Wars: The Last Jedi.")
        elif choice6a == "b" or choice6a == "B":
            print("Jeff follows her. Kat turns the handle to the restroom door when she feels someone grab her arm. She turns around and sees Jeff. Jeff pushes her into the bathroom and closes the door. He then strangles her and Kat dies. Jeff walks out and leaves the party.")
    elif choice5a == "b" or choice5a == "B":
            print("Jeff decides he would rather not talk to her. He stays with his friends and continues to drink more. Jeff gets drunk and stumbles outside onto the balcony for some fresh air. He sees Verne and Kat in the yard. He looks over the balcony but leans too far and falls to his death. The end.")
    elif choice2a == "b" or choice2a == "B":
            print("You stay home and play video games. The end.")        
elif choice1 == "b" or choice1 == "B":
    print("You are Verne and you study at Pug University and Verne's best friends are Kat, Rachelle, and Jacky. They are going to a party(Same one Jeff will be at).")
    print("Once you arrive at the party, you have a choice to be responsible and not drink.")
    print("Choice A: Drink.")
    print("Choice B: Doesn't drink")
    choice3a = raw_input("Drink or not drink?: ")
    if choice3a == "a" or choice3a == "A":
        print("Verne is drunk and she cant walk straight and she encounters Jeff and he guides her to the backyard where he kills her.The end.")
    elif choice3a == "b" or choice3a == "B":
        print("Verne keeps an eye out and will be the one responsible on taking her and her best friends home.")
        print("Verne notices Kat is being flirty with Jeff, she ignores them and goes around the house and finds a guy named Jimin and her heart starts to flutter.")
        print("Verne and Jimin start talking and Jimin asks her if she has a boyfriend,Verne responds and says no.")
        print("Verne wants to kiss the guy, but she doesn't know if she should.")
        print("You have a choice kiss or not.")
        print("choice A:Kiss")
        print("Choice B:Dont kiss")
        choice4a = raw_input("Kiss or not?: ")
        if choice4a == "a" or choice4a == "A":
            print("Verne kisses him and they talk the whole night and then she ends up falling asleep next to him on sofa couch in his room.")
            print("The next day Verne wakes up and remembers about her freinds, and she finds Rachelle and Jacky knocked out on the couch and she searches for Kat and you find her dead on the floor in the restroom.")
            print("Verne runs and calls her friends and calls 911.")
            print("The cops arrive and ask everyone to leave the premises.")
            print("The cops say they will take the body and find out what happened..To be continued.")
        elif choice4a == "b" or choice4a == "B":
            print("It gets awkward and Verne looks for her freinds and asks if they're ready to go and they say no and Verne goes to look for Kat and notices Jeff coming out of the restroom and sees Kat unconcious on the floor.")
            print("Jeffs hadn't seen Verne, because she was able to hide in the closet quickly and Verne dials 911.. and Jeff opens the door..To be continued.")