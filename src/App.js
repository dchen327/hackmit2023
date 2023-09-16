import "bulma/css/bulma.min.css";

import { useState, useEffect, useRef } from "react";
import Fraction from "fraction.js";

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

  // const handleNewPuzzleClick = async () => {
  //   setShowModal(false);
  //   const response = await fetch("/api/index.py", {
  //     method: "POST",
  //     headers: {
  //       "Content-Type": "application/json",
  //     },
  //     body: JSON.stringify({ params: "hi" }),
  //   });
  //   const data = await response.json();

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

  const products = [
    { id: 1, name: 'Product 1', price: 19.99 },
    { id: 2, name: 'Product 2', price: 29.99 },
    { id: 3, name: 'Product 3', price: 39.99 },
    // Add more products as needed
  ];

  // search functionality 
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleSearch = () => {
    // You can implement your search functionality here
    console.log('Searching for:', searchTerm);
  };

  return (
    <div className="container">
      <h1 className="title">title</h1>
      <div className="field has-addons">
        <div className="control">
          <input className="input" type="text" placeholder="Search" />
        </div>
        <div className="control">
          <button className="button is-primary ml-2" onClick={handleSearch}>
            Search
          </button>
        </div>
      </div>

      {/* <div className="container"> */}

      <div>
        {products.map((product) => (
          <div key={product.id} className="box">
            <h2 className="title is-4">{product.name}</h2>
            <p className="subtitle is-6">${product.price.toFixed(2)}</p>
            {/* You can add more product details here */}
            <button className="button is-primary">Add to Cart</button>
          </div>
        ))}
      </div>

      {/* </div> */}

    </div>


  );
}

export default App;
