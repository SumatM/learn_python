import { StatusBar } from "expo-status-bar";
import { useState } from "react";
import { Alert, StyleSheet, Text, TouchableOpacity, View } from "react-native";

export default function App() {
  const [count, setCount] = useState(0);

  const add = () => {
    setCount(count + 1);
  };

  const dec = () => {
    if(count>0){
      setCount(count - 1);
    }else{
      Alert.alert('Count Alert', 'Count cannot be negative!', [{ text: 'OK' }]);

    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.text}>Counter App</Text>
      <Text style={styles.count}>{count}</Text>
      <View>
        <TouchableOpacity style={styles.button} onPress={add}>
          <Text style={styles.buttonText}>Increment</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.button} onPress={dec}>
          <Text style={styles.buttonText}>Decrement</Text>
        </TouchableOpacity>
      </View>
      <StatusBar style="auto" />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#fff",
    alignItems: "center",
    marginTop:"50%"
  },
  text: {
    fontSize: 40,
    padding: "25px",
    fontWeight: "bold",
  },
  count: {
    fontSize: 80,
    fontWeight: "bold",
    marginTop:25
  },
  button: {
    backgroundColor: "black",
    padding:10,
    marginTop:18,
  },
  buttonText:{
    color:'white',
    fontSize:16,
    fontWeight:'bold'
  }
});
