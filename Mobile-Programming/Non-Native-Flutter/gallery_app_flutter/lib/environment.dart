const _baseUrl = "baseUrl";

enum Environment { dev, prod }

Map<String, dynamic> _config;

void setEnv(Environment env) {
  switch (env) {
    case Environment.dev:
      _config = _devConfig;
      break;
    case Environment.prod:
      _config = _prodConfig;
      break;
  }
}


dynamic get apiBaseUrl => _config[_baseUrl];


Map<String, dynamic> _devConfig = {
  _baseUrl: "http://10.0.2.2:8080/api/"
};

Map<String, dynamic> _prodConfig = {
  _baseUrl: "http://10.0.2.2:8080/api/"
};