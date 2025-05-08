# gRPC
Trying gRPC for multiple docker containers

# File structure

There are 3 main folders: 
- **Doc**: which contains a functional calculator app
- **serializarionWithoutDocker**: causal nest implementation without usage of docker
- **src**: contains apps with the docker implementation
```
.
├── doc
│   └── README.md
├── LICENSE
├── serializarionWithoutDocker
│   └── README.md
├── src
│   ├── calculator
│   │   └── README.md
│   └── causalNestDockerPickle
│       └── README.md
└── README.md
```

The most important ones are the `causalNestDockerPickle` and `serializarionWithoutDocker`: both folders contain the implementation for the causal nest mock library, using or not docker. 

Further explanation for each folder is given in their READMEs.
