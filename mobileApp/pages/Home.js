/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import type, {Node} from 'react';
import {
    ImageBackground,
    SafeAreaView,
    ScrollView,
    StatusBar,
    StyleSheet,
    Text,
    useColorScheme,
    View,
    Pressable,
    Image, Dimensions, Button,
} from 'react-native';

import {
    Colors,
    DebugInstructions,
    Header,
    LearnMoreLinks,
    ReloadInstructions,
} from 'react-native/Libraries/NewAppScreen';
import {collectCoverage} from "simctl/jest.config";
import LoginButton from "./Button";

const Home: () => Node = () => {
    const isDarkMode = useColorScheme() === 'dark';

    const backgroundStyle = {
        backgroundColor: isDarkMode ? Colors.darker : Colors.lighter,
    };

    return (
        <View style={{flex:1}}>
            <ImageBackground source={ require('../static/backgroundImg.jpeg')} style={styles.image} >
                <Text style={styles.sectionTitle}>
                    Attune
                </Text>
                <LoginButton></LoginButton>
            </ImageBackground>
        </View>
    );
};

const styles = StyleSheet.create({


    MainContainer: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    image: {
        backgroundRepeat: 'noRepeat',
        backgroundSize: 'cover',
        backgroundPosition: 'center',
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
    },
    sectionContainer: {
        marginTop: 32,
        paddingHorizontal: 24,
    },
    sectionTitle: {
        fontSize: 80,
        fontWeight: '600',
        paddingBottom: 60,
        fontColor: 'charcoal',
    }
    ,});

export default Home;
