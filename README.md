![bolinha_fofinha](https://github.com/michellopes338/LiveEye/assets/71197700/da5a0f0a-6897-4c98-9ea0-634975b89a5f)
# LiveEye

LiveEye is a Python script designed to monitor the status of a livestream and automatically open the stream when the streamer goes live.

## Features
- **Livestream Monitoring:** Continuously checks the status of the livestream to detect when the streamer starts broadcasting.
- **Automatic Stream Opening:** Automatically opens the livestream in the default browser when the streamer goes live.

## Working Features
- **Customizable Timeout:** Ability to set a timeout for how often the script checks the livestream status.
- **Supports Multiple Platforms:** Designed to work with various livestreaming platforms.

## Getting Started
### Prerequisites
- Python 3.x installed on your system.
- Internet connection to monitor livestream status.

### Installation
1. Clone the repository to your local machine:
~~~
git clone https://github.com/michellopes338/LiveEye.git
~~~
3. Navigate to the project directory:
~~~
cd LiveEye
~~~
5. Install dependencies:
~~~
pip install -r requirements.txt
~~~

### Usage
1. Open a terminal and navigate to the project directory.
2. Run the script with the desired parameters:
~~~
python main.py --streamer cellbit
~~~
3. The script will continuously monitor the livestream status. When the streamer goes live, the livestream will automatically open in your default web browser.

## Configuration
- **Timeout:** You can adjust the timeout duration by specifying the --timeout parameter when running the script. The default timeout is set to 10 minutes.

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
