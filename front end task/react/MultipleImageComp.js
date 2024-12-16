import React, { Component } from 'react';
import gill from '../Assests/3.jpg';
import abishek from '../Assests/4.jpg';
import bumrah from '../Assests/5.jpeg'; 

class MultipleImageComp extends Component {
    constructor(props) {
        super(props);
        this.state = {
            selectedImage: null,  
        };
    }

    toggleImage = (image) => {
        this.setState({ selectedImage: image });
    };

    render() {
        return (
            <div>
                <h2>Multiple Image with Name</h2>

                {this.state.selectedImage && (
                    <div style={{ marginTop: '20px' }}>
                        <h3>{this.state.selectedImage.alt}</h3>
                        <img
                            src={this.state.selectedImage.src}
                            alt={this.state.selectedImage.alt}
                            height='200px'
                            width='200px'
                        />
                    </div>
                )}

                
              
                <button
                    onClick={() => this.toggleImage({ src: gill, alt: 'gill' })}
                    className="btn btn-primary"
                    style={{ marginTop: '10px', marginRight: '10px' }}
                >
                    Show gill
                </button>
                <button
                    onClick={() => this.toggleImage({ src: abishek, alt: 'abishek' })}
                    className="btn btn-primary"
                    style={{ marginTop: '10px', marginRight: '10px' }}
                >
                    Show abishek
                </button>
                <button
                    onClick={() => this.toggleImage({ src: bumrah, alt: 'bumrah' })}
                    className="btn btn-primary"
                    style={{ marginTop: '10px', marginRight: '10px' }}
                >
                    Show bumrah
                </button>
            </div>
        );
    }
}

export default MultipleImageComp;