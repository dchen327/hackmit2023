// Routes.js
import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import MainPage from './App';
import PostPage from './PostPage';

function Routes() {
  return (
    <Router>
      <Switch>
        <Route exact path="/" component={MainPage} />
        <Route path="/plus" component={PostPage} />
      </Switch>
    </Router>
  );
}

export default Routes;
