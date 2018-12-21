import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';

export default class App extends React.Component {
  render() {
    return (
      <View style={styles.container}>
        <Text>Open up App.js to start working on your app!</Text>
        <Image style={{width:200, height:200}} source={{uri:'http://3.bp.blogspot.com/-nXPldUWrd8c/Uby3E2T5NvI/AAAAAAAAAJ4/FFL6dLO8JoQ/s1600/Tintin+-+Professeur+Tryphon+Tournesol_XL.jpg'}}></Image>
        <Text>HELLOOOOO</Text>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
