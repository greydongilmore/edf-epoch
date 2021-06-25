<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/greydongilmore/edf-epoch">
    <img src="imgs/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">edf epoch</h3>

  <p align="center">
    EDF+ epoch creation tool
    <br />
    <a href="https://github.com/greydongilmore/edf-epoch"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/greydongilmore/edf-epoch/issues">Report Bug</a>
    ·
    <a href="https://github.com/greydongilmore/edf-epoch/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This code snippet will create an epoch from an EDF+ file given a start and end time in seconds.

### Built With

* Python version: 3.9


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

No Prerequisites required. Any Python3 version will suffice.

### Installation

1. In a terminal, clone the repo by running:
   ```sh
   git clone https://github.com/greydongilmore/edf-epoch.git
   ```

2. Change into the project directory (update path to reflect where you stored this project directory):
  ```sh
  cd /home/user/Documents/Github/edf-epoch
  ```

3. Install the required Python packages:
  ```sh
  python -m pip install -r requirements.txt
  ```


<!-- USAGE EXAMPLES -->
## Usage

1. In a terminal, move into the project directory
   ```sh
   cd /home/user/Documents/Github/edf-epoch
   ```

2. Run the following to execute the epoch script:
  ```sh
  python main.py -i "full/path/to/edf/file" -s 10 -e 400
  ```

  * **-i:** full file path to the EDF file you want to epoch
  * **-s:** starting time for the epoch (in seconds)
  * **-e:** ending time for the epoch (in seconds)


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Greydon Gilmore - [@GilmoreGreydon](https://twitter.com/GilmoreGreydon) - greydon.gilmore@gmail.com

Project Link: [https://github.com/greydongilmore/edf-epoch](https://github.com/greydongilmore/edf-epoch)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* README format was adapted from [Best-README-Template](https://github.com/othneildrew/Best-README-Template)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/greydongilmore/edf-epoch.svg?style=for-the-badge
[contributors-url]: https://github.com/greydongilmore/edf-epoch/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/greydongilmore/edf-epoch.svg?style=for-the-badge
[forks-url]: https://github.com/greydongilmore/edf-epoch/network/members
[stars-shield]: https://img.shields.io/github/stars/greydongilmore/edf-epoch.svg?style=for-the-badge
[stars-url]: https://github.com/greydongilmore/edf-epoch/stargazers
[issues-shield]: https://img.shields.io/github/issues/greydongilmore/edf-epoch.svg?style=for-the-badge
[issues-url]: https://github.com/greydongilmore/edf-epoch/issues
[license-shield]: https://img.shields.io/github/license/greydongilmore/edf-epoch.svg?style=for-the-badge
[license-url]: https://github.com/greydongilmore/edf-epoch/blob/master/LICENSE.txt
