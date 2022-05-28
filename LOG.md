# Dev Log

## 2022-05 28

This was much too much effort. Going back to the original, I now accept `world` as a module global.


## 2022-05-15

When importing morphic.py as a module in `card.py`, it doesn't work because `world` is used as a global variable in many places.

I want to hunt this down. As an example, I create a rectangle, using the context menu:

![Create rectangle](images/create-rectangle.png)

This invokes function `user_create_rectangle`.

In it, `pick_up()` needs to get the world as parameter. In `morphic.js` it does so. I have added the world as optional parameter to `pick_up()`. With this, creating a rectangle from the dev menu works :)

Also, `Menu.pupup_at_hand()` needs the world as parameter. This is no problem, because it is invoked from the hand which knows its world.

