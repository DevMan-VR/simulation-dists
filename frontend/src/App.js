import logo from './logo.svg';
import './App.css';
import NeuroCard from './components/NeuroCard/NeuroCard';
function App() {
  return (
    <div className="App">
      <div style={styles.mainContainer}>
        <NeuroCard backgroundColor={"#E4F1FA"} height={"70%"} width={"50%"} borderRadius={'2em'}>
          <div>
          </div>
        </NeuroCard>

      </div>
      
    </div>
  );
}

const styles = {
  mainContainer: {
    width: '100vw',
    height: '100vh',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#6483A0'
  }
}

export default App;
