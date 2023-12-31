# XBeeComms

Introduction
  ------------
  This is a sample python application aims to send and receive data using Xbee devices defined by MAC addresses and joined to the same Zigbee network

  This Example is nothing more than using Digicom Xbee python library.
  We aim to send periodically a blocking trasmit request and notification will be received if any error during the process is happened.

  Requirements
  ------------
  To run this example you will need:

    * At least two XBee radios in API mode and their corresponding carrier
      board.
    * The XCTU application (available at www.digi.com/xctu).

  Compatible protocols
  --------------------
    * 802.15.4
    * DigiMesh
    * Point-to-Multipoint
    * Zigbee


  Example setup
  -------------
    1) Plug the XBee radios into the XBee adapters and connect them to your
       computer's USB or serial ports.

    2) Configure the remote XBee device with the Node Identifier used by the
       example to communicate with it. To do so follow these steps:

          1) Launch the XCTU application.

          2) Add the remote XBee module to the XCTU, specifying it's port
             settings.

          3) Once the module is added, open the 'Configuration' working mode,
             look for the 'NI' setting and configure it with 'REMOTE'
             (without quotes).

             Notice that by default the 'NI' setting has a blank space
             configured, make sure that there is not a blank space before the
             'REMOTE' text.

    3) Ensure that the modules are in API mode and on the same network.
       For further information on how to perform this task, read the
       'Configuring Your XBee Modules' topic of the Getting Started guide.

    4) Set the port and baud rate of the sender (local) XBee radio in the
       sample file.
       If you configured the modules in the previous step with the XCTU, you
       will see the port number and baud rate in the 'Port' label of the device
       on the left view.


  Running the example
  -------------------
  First, build the application. Then, you need to setup XCTU to see the data
  received by the remote XBee device. Follow these steps to do so:

    1) Before running the script :
    install requirements by running this command :
    '''
    sudo pip install -r requirements.txt
    '''

    1) Launch the XCTU application.

    2) Add the remote XBee module to the XCTU, specifying it's port settings.

    3) Switch to the 'Consoles' working mode and open the serial connection
       so you can see the data when it is received.

  Finally, launch the sample application, some data is sent to the configured
  remote XBee device whose Node Identifier is 'REMOTE'. When that happens, a
  line with the result of the operation is printed to the standard output:

    Sending data to 0013A20040XXXXXX >> Hello XBee!...
    Success

     - Where 0013A20040XXXXXX is the 64-bit address of the remote XBee device
       whose Node Identifier is 'REMOTE'.

  Verify that in the XCTU console a new RX frame has been received by the
  remote XBee device. Select it and review the details, some of the details
  will be similar to:

    - Start delimiter:         7E
    - Length:                  Depends on the XBee protocol.
    - Frame type:              Depends on the XBee protocol.
    - 64-bit source address:   The XBee sender's 64-bit address.
    - RF data/Received data:   48 65 6C 6C 6F 20 58 42 65 65 21
                               Hello XBee!
