import socket 
import sys
import threading
banner = ''' 
                     __  __ _ _   _                         _ _      
                    |  \/  (_) | | |                       | (_)     
                    | \  / |_| |_| |__  _ __ __ _ _ __   __| |_ _ __ 
                    | |\/| | | __| '_ \| '__/ _` | '_ \ / _` | | '__|
                    | |  | | | |_| | | | | | (_| | | | | (_| | | |   
                    |_|  |_|_|\__|_| |_|_|  \__,_|_| |_|\__,_|_|_|
                    
                        "Not all those who wander are lost"\n\n
'''

success_banner = '''
                                Three::rings
                            for:::the::Elven-Kings
                        under:the:sky,:Seven:for:the
                        Dwarf-Lords::in::their::halls:of
                        stone,:Nine             for:Mortal
                    :::Men:::     ________     doomed::to
                    die.:One   _,-'...:... `-.    for:::the
                    ::Dark::  ,- .:::::::::::. `.   Lord::on
                    his:dark ,'  .:::::zzz:::::.  `.  :throne:
                    In:::the/    ::::dMMMMMb::::    \ Land::of
                    :Mordor:\    ::::dMMmgJP::::    / :where::
                    ::the::: '.  '::::YMMMP::::'  ,'  Shadows:
                    lie.::One  `. ``:::::::::'' ,'    Ring::to
                    ::rule::    `-._```:::_,-'     ::them::
                    all,::One      `-----'        ring::to
                    ::find:::                  them,:One
                        Ring:::::to            bring::them
                        all::and::in:the:darkness:bind
                            them:In:the:Land:of:Mordor
                            where:::the::Shadows
                                    :::lie.:::
'''

firework = '''
               *    *
   *         '       *       .  *   '     .           * *
                                                               '
       *                *'          *          *        '
   .           *               |               /
               '.         |    |      '       |   '     *
                 \*        \   \             /
       '          \     '* |    |  *        |*                *  *
            *      `.       \   |     *     /    *      '
  .                  \      |   \          /               *
     *'  *     '      \      \   '.       |
        -._            `                  /         *
  ' '      ``._   *                           '          .      '
   *           *\*          * .   .      *
*  '        *    `-._                       .         _..:='        *
             .  '      *       *    *   .       _.:--'
          *           .     .     *         .-'         *
   .               '             . '   *           *         .
  *       ___.-=--..-._     *                '               '
                                  *       *
                *        _.'  .'       `.        '  *             *
     *              *_.-'   .'            `.               *
                   .'                       `._             *  '
   '       '                        .       .  `.     .
       .                      *                  `
               *        '             '                          .
     .                          *        .           *  *
             *        .                                    '

'''
class Mithrandir_Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def listen(self):
        print("[*] Mithrandir listening on 2941")
        self.socket.bind(('0.0.0.0', 2941))
        self.socket.listen(5)

        while True:
            client_socket, addr = self.socket.accept()

            client_thread = threading.Thread(target=self.handle, args=(client_socket,))
            client_thread.start()

    def handle(self, client_socket):
        client_socket.sendall(banner.encode("UTF-8"))
        client_socket.sendall(b'Here are your available commands:\n\ndefeat_sauron\nlaunch_fireworks\ncredits\nhelp\n')
        commands = ['defeat_sauron', 'launch_fireworks', 'credits', 'help']
        while True:
            try:
                data = client_socket.recv(1024)
                input = data.decode().strip()
                if input in commands:
                    if input == 'defeat_sauron':
                        output = self.defeat_sauron(client_socket,)
                        client_socket.sendall(output.encode("UTF-8"))
                    if input == 'launch_fireworks':
                        output = self.launch_fireworks()
                        client_socket.sendall(output.encode("UTF-8"))
                    if input == 'credits':
                        output = self.credits()
                        client_socket.sendall(output.encode("UTF-8"))
                    elif input == 'help':
                         client_socket.sendall(b'\nHere are your available commands:\n\ndefeat_sauron\nlaunch_fireworks\ncredits\nhelp\n')                 
                else:
                    client_socket.sendall(b"\nError: type 'help' to view acceptable commands.")

            except KeyboardInterrupt:
                print('User terminated.')
                self.socket.close()
                sys.exit()
    def defeat_sauron(self, client_socket):
        client_socket.sendall(b'Hello Gandalf, please enter your password:')
        data = client_socket.recv(1024)
        passwd = data.decode().strip()
        if passwd != 'Th3_WhIt3_R1d3r_24!':
           return '[*] Error: invalid credentials \n' +  '[*] Exiting...\n'
        else: 
           return success_banner + '\n\n\nFlag: summitCTF{OS1NT_S4v3d_M1ddl3_E4rTh}'

    def launch_fireworks(self):
        return firework
    def credits(self):
        return "\nCredits to the grey pilgrim: \n\n @0xGreyPilgrim"
server = Mithrandir_Server()
server.listen()