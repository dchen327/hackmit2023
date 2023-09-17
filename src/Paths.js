// Routes.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './App';
import PostPage from './PostPage';

function Paths() {
  return (
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/post" element={<PostPage />} />
      </Routes>
  );
}

export default Paths;
