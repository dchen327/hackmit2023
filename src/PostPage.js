import "bulma/css/bulma.min.css";
import React from 'react';
import { useState, useEffect, useRef } from "react";
import { Link } from 'react-router-dom';

function PostPage() {

    // post functionality

    const [postTerm, setPostTerm] = useState("");

    const handlePost = async () => {
      setPostTerm("");
      const response = await fetch("/api/post.py", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          itemName: postTerm,
          title,
          description,
          startDate,
          endDate,
          price
        }),
      });
      const data = await response.json();
    };

  //item information
  const [description, setDescription]=useState("")
  const [title, setTitle] = useState("");
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [price, setPrice] = useState("");
  const [contact, setContact] = useState("");

  //methods for setting item info
  const handleTitleChange = (e) => {
    setTitle(e.target.value);
  };
  const handleDescriptionChange = (e) => {
    setDescription(e.target.value);
  };
  const handleContactChange = (e) => {
    setContact(e.target.value);
  }


  return (
    <div className="container">
      <h1 className="title mt-4">Post Your Item</h1>
    <div>
      <label className="label">Post Title</label>
      <div className="field has-addons">
        <div className="control">
          <input
            className="input"
            type="text"
            placeholder="What is your item?"
            onChange={handleTitleChange}
          />
        </div>
      </div>

      <label className="label">Description</label>
      <div className="field has-addons">
        <div className="control">
          <input
            className="input"
            style={{ width: '90vw'}}
            type="text"
            placeholder="Description of your item!"
            onChange={handleDescriptionChange}
          />
        </div>
      </div>

      <div className="columns">
        <div className="column">
          <div className="field">
            <label className="label">Date Availability Starts</label>
            <div className="control">
              <input
                className="input"
                type="date"
                value={startDate}
                onChange={(e) => setStartDate(e.target.value)}
              />
            </div>
          </div>
        </div>
        <div className="column">
          <div className="field">
            <label className="label">Date Availability Ends</label>
            <div className="control">
              <input
                className="input"
                type="date"
                value={endDate}
                onChange={(e) => setEndDate(e.target.value)}
              />
            </div>
          </div>
        </div>
        <div className="column">
          <div className="field">
            <label className="label">Price</label>
            <div className="control">
              <input
                className="input"
                type="number"
                value={price}
                onChange={(e) => setPrice(e.target.value)}
              />
            </div>
          </div>
        </div>
          </div>
      <label className="label">Contact Information</label>
      <div className="field has-addons">
        <div className="control">
          <input
            className="input"
            type="text"
            placeholder="Your email"
            onChange={handleTitleChange}
          />
        </div>
      </div>

        <div className="field">
            <label className="label has-text-white">`</label>
            <div className="control">
            <Link to='/'> 
              <button
                className="button is-primary"
                onClick={handlePost} // Add your submit function here
              >
                Post
              </button>
              </Link>
            </div>
    </div>
    </div>
    </div>
  );
}

export default PostPage;