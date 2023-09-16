import "bulma/css/bulma.min.css";

import { useState, useEffect, useRef } from "react";

function App() {
  // const [selectedNumberIdx, setSelectedNumberIdx] = useState(null);
  // const [selectedOpIdx, setSelectedOpIdx] = useState(null);
  // const [gameNums, setGameNums] = useState([
  //   new Fraction(2),
  //   new Fraction(3),
  //   new Fraction(4),
  //   new Fraction(6),
  // ]);
  // const [originalGameNums, setOriginalGameNums] = useState([
  //   new Fraction(2),
  //   new Fraction(3),
  //   new Fraction(4),
  //   new Fraction(6),
  // ]);
  // const [showModal, setShowModal] = useState(false);
  // const [gameHistory, setGameHistory] = useState([]);
  // const operations = ["+", "-", "x", "÷"];
  // const numberButtonsRef = useRef(null);
  // const opButtonsRef = useRef(null);

  // useEffect(() => {
  //   const handleClickOutside = (event) => {
  //     if (
  //       numberButtonsRef.current &&
  //       !numberButtonsRef.current.contains(event.target) &&
  //       opButtonsRef.current &&
  //       !opButtonsRef.current.contains(event.target)
  //     ) {
  //       setSelectedNumberIdx(null);
  //       setSelectedOpIdx(null);
  //     }
  //   };
  //   document.addEventListener("click", handleClickOutside);
  //   return () => {
  //     document.removeEventListener("click", handleClickOutside);
  //   };
  // }, []);

  // useEffect(() => {
  //   if (
  //     gameNums.filter((num) => num !== "").length === 1 &&
  //     gameNums.some((num) => num && num.valueOf() === 24)
  //   ) {
  //     setShowModal(true);
  //   }
  // }, [gameNums]);

  // const handleNumberClick = (idx) => {
  //   if (
  //     gameNums[idx] !== "" &&
  //     selectedNumberIdx !== null &&
  //     selectedOpIdx !== null
  //   ) {
  //     const num1 = gameNums[selectedNumberIdx];
  //     const num2 = gameNums[idx];
  //     let result;
  //     switch (selectedOpIdx) {
  //       case 0:
  //         result = num1.add(num2);
  //         break;
  //       case 1:
  //         result = num1.sub(num2);
  //         break;
  //       case 2:
  //         result = num1.mul(num2);
  //         break;
  //       case 3:
  //         result = num1.div(num2);
  //         break;
  //     }
  //     setSelectedNumberIdx(idx);
  //     setSelectedOpIdx(null);
  //     setGameNums((prevNums) => {
  //       const newNums = [...prevNums];
  //       newNums[idx] = result;
  //       newNums[selectedNumberIdx] = "";
  //       return newNums;
  //     });
  //     setGameHistory((prevHistory) => [...prevHistory, gameNums]);
  //   } else if (gameNums[idx] !== "") {
  //     setSelectedNumberIdx(idx);
  //   }
  // };

  // const handleOpClick = (idx) => {
  //   setSelectedOpIdx(idx);
  // };

  // const handleResetClick = () => {
  //   setGameNums(originalGameNums);
  //   setSelectedNumberIdx(null);
  //   setSelectedOpIdx(null);
  //   setGameHistory([]);
  // };

  // const handleUndoClick = () => {
  //   if (gameHistory.length > 0) {
  //     const prevGameNums = gameHistory[gameHistory.length - 1];
  //     setGameNums(prevGameNums);
  //     setGameHistory((prevHistory) => prevHistory.slice(0, -1));
  //     setSelectedNumberIdx(null);
  //     setSelectedOpIdx(null);
  //   }
  // };

  //   const newGameNums = data.gameNums.map((num) => new Fraction(num));

  //   setGameNums(newGameNums);
  //   setOriginalGameNums(newGameNums);
  //   setSelectedNumberIdx(null);
  //   setSelectedOpIdx(null);
  //   setGameHistory([]);
  // };

  // const handleHintClick = () => {
  //   // TODO: Implement hint functionality
  //   console.log("Hint clicked");
  // };
  const supply = [
    {
      itemName: "TV",
      startDate: "09/01/2023",
      endDate: "10/01/2023",
      price: 50,
      pictures: [],
      contact: "test@college.edu",
      addlNotes: "Here are some notes",
    },
    {
      itemName: "TV",
      startDate: "10/01/2023",
      endDate: "11/01/2023",
      price: 50,
      pictures: [],
      contact: "test@college.edu",
      addlNotes: "",
    },
  ];

  const [matches, setMatches] = useState([]);

  const products = [
    { id: 1, name: "Product 1", price: 19.99 },
    { id: 2, name: "Product 2", price: 29.99 },
    { id: 3, name: "Product 3", price: 39.99 },
    // Add more products as needed
  ];

  // search functionality
  const [searchTerm, setSearchTerm] = useState("");

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearch = async () => {
    setSearchTerm("");
    const response = await fetch("/api/search.py", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        itemName: searchTerm,
        startDate,
        endDate,
        maxPrice,
      }),
    });
    const data = await response.json();
    setMatches(data["itemMatches"]);
  };

  // search filters
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [maxPrice, setMaxPrice] = useState("");
  const [showFilter, setShowFilter] = useState(false);

  const toggleShowFilter = () => {
    setShowFilter(!showFilter);
  };
  // // interested button functionality
  // const [buttonText, setButtonText] = useState("I'm interested");
  // const [buttonColor, setButtonColor] = useState("is-primary");

  // const handleInterestedButtonClick = () => {
  //   setButtonText("Owner notified!");
  //   setButtonColor("is-success"); // Change the color to a success color
  // };

  return (
    <div className="container">
      <h1 className="title mt-4">Summer Saver</h1>
      <label className="label">Search by item name</label>
      <div className="field has-addons">
        <div className="control">
          <input
            className="input"
            type="text"
            placeholder="Search"
            onChange={handleSearchChange}
          />
        </div>
      </div>

      <div className="columns">
  <div className="column">
    <div className="field">
      <label className="label">Start Date</label>
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
      <label className="label">End Date</label>
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
      <label className="label">Maximum Price</label>
      <div className="control">
        <input
          className="input"
          type="number"
          value={maxPrice}
          onChange={(e) => setMaxPrice(e.target.value)}
        />
      </div>
    </div>
  </div>
  <div className="column">
    <div className="field">
    <label className="label has-text-white">`</label>
      <div className="control">
        <button
          className="button is-primary"
          onClick={handleSearch} // Add your submit function here
        >
          Search
        </button>
      </div>
    </div>
  </div>
</div>


      {/* <div className="control">
          <button className="button is-primary ml-2" onClick={handleSearch}>
            Search
          </button>
        </div> */}

      {/* <div className="container"> */}

      <div>
        
        { matches.length == 0 ? <p>No results found, did you mean 'fridge'?</p> : <h1 className="subtitle">Results for {searchTerm}</h1>}
        {matches.map((item, idx) => (
          <div key={`match{${idx}}`} className="box">
            <div className="columns">
              {/* Left Column (Content) */}
              <div className="column">
                <h2 className="title is-4">{item.itemName}</h2>
                <div className="">
                  <p className="is-6">
                    <strong>Price: </strong> ${item.price}
                  </p>
                  <p className="is-6">
                    <strong>Dates Offered: </strong>{" "}
                    {`${item.startDate} - ${item.endDate}`}
                  </p>
                  <p className="is-6">
                    <strong>Notes: </strong> {item.addlNotes}
                  </p>
                  <p className="is-6">
                    <strong>Contact: </strong> {item.contact}
                  </p>
                  <p></p>
                </div>
              </div>
              {/* Right Column (Image) */}
              <div className="column is-one-third">
                <figure className="image is-128x128">
                  <img
                    src={require("./images/" + item.pictures[0])}
                    alt="Item Image"
                  />
                </figure>
              </div>
            </div>
          </div>
        ))}
      </div>

      {/* </div> */}
    </div>
  );
}

export default App;
