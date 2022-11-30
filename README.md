# Ultimate TicTacToe
This project is a simple implementation of Ultimate Tic-Tac-Toe. It uses [PyGame](https://www.pygame.org/wiki/about), a python library for creating games.
## Game Rules
- The game is composed of nine tic-tac-toe boards, arranged in a 3x3 grid. Each of these tic-tac-toe boards are referred to as a local board, while the larger 3x3 is refered to as the global board.

![image](https://user-images.githubusercontent.com/104611224/204930232-ae95473a-3098-4014-87ac-d1f4fa25c976.png)

- Where the user plays on the local board determines where they play on the global board. In this implementation, where the user may go is highlighted green. The game starts with all local boards available for play.
  - For example, if the user plays in the top corner of a local board, then play will move to the top corner of the global board.
  
 ![image](https://user-images.githubusercontent.com/104611224/204930718-56142b9d-4bea-4f27-ba29-1c9e7d71a69b.png)
- Once a local board has been won or filled, no more moves can be played there. If a move would place a player on such a board, then that player may place their move on any other available board.

![image](https://user-images.githubusercontent.com/104611224/204931218-81e63e2b-7024-4a05-b612-ba6dbe55e4d3.png)

- The game is over once the global board has been won, or once no legal moves may be placed

![image](https://user-images.githubusercontent.com/104611224/204931754-5f28330a-9f45-4232-b491-724799b5ea43.png)
