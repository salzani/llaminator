def get_style() -> str:
        return """
            QWidget {
                background-color: #f5f5f5;
            }
            
            #backgroundContainer {
                background-image: url("assets/img/llaminator.jpeg");
                background-repeat: no-repeat;
                background-position: center;
                background-size: 50% auto;
                padding: 10px;
            }
            
            #chatDisplay {
                background-color: rgba(255, 255, 255, 0.8);
                padding: 6px;
                border: 1px solid #ccc;
                border-radius: 8px;
            }

            #chatDisplay p {
                margin-bottom: 50px;
                margin-top: 0px;
                padding: 0px;
             }
            
            #inputField {
                background-color: rgba(255, 255, 255, 0.9);
                border: 1px solid #ccc;
                border-radius: 8px;
                padding: 6px;
            }
            
            #sendButton {
                background-color: #0078d7;
                color: white;
                border-radius: 8px;
                padding: 8px 16px;
            }
            
            #sendButton:hover {
                background-color: #005fa3;
            }
        """