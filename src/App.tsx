import { useState } from 'react';
import './App.css';
import Blog from './components/blog/Blog';
import Container from '@mui/material/Container';
import theme from './theme';
function App() {
  const [count, setCount] = useState(0);

  return (
    // <div className="App">
    <Container maxWidth="lg">
      <Blog />
    </Container>
    // </div>
  );
}

export default App;
