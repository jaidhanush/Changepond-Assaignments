import React, { Component } from "react";

import chepauk from '../Assests/chepauk.jpeg';
import chinnaswamy from '../Assests/chinnaswamy.jpeg';

class Toggletask extends Component {
  constructor(props) {
    super(props);
    this.state = {
      imageSrc: chepauk,
      imageAlt: "chepauk",
      stadiumName: "Chepauk Stadium",
    };
  }

  toggleImage = () => {
    const { imageAlt } = this.state;

    if (imageAlt === "chepauk") {
      this.setState({
        imageSrc:chinnaswamy,
        imageAlt: "chinnaswamy",
        stadiumName: "Chinnaswamy Stadium",
      });
    } else {
      this.setState({
        imageSrc: chepauk,
        imageAlt: "chepauk",
        stadiumName: "Chepauk Stadium",
      });
    }
  };

  render() {
    const { imageSrc, imageAlt, stadiumName } = this.state;

    return (
      <div className="centered-content">
        <img src={imageSrc} alt={imageAlt} id="image" className="image-box" />
        <h2 id="stadium-name">{stadiumName}</h2>
        <button type="button" onClick={this.toggleImage} className="btn btn-primary">
          Click me
        </button>
      </div>
    );
  }
}

export default Toggletask;
