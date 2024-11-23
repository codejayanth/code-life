package main

import (
	"fmt"
	"io/ioutil"
	"log"

	"gopkg.in/yaml.v3"
)

type YamlData struct {
	Guid        string   `yaml:"guid"`
	Description string   `yaml:"description"`
	IsCanonical bool     `yaml:"is_canonical"`
	Implements  []string `yaml:"implements"`
}

func YamlReader() ([]byte, error) {
	data, err := ioutil.ReadFile("/Users/ramajayanth/Downloads/AHU.yaml")
	if err != nil {
		log.Println("The error is %v", err)
	}

	// fmt.Println("The data is: ", string(data))

	return data, err
}

func main() {
	data, err := YamlReader()
	if err != nil {
		log.Println("The error is:", err)
	}
	// fmt.Println("The yaml data is:", string(data))

	var blog map[string]interface{}
	err = yaml.Unmarshal(data, &blog)
	if err != nil {
		panic(err)
	}

	// fmt.Println("The unmarshalled data is:", yamlD)
	//fmt.Printf("%+v\n", blog)

	out, err := yaml.Marshal(blog)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Printf(string(out))

}
