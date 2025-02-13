#pragma once
#include "./common.hpp"
#include "./Request.hpp"

class Request;

class Cgi
{
	private:
		//int _fd;
		pid_t _pid;
		char **_argv;
		char **_envp;
		int _pipeFd[2];
		int _responsePipeFd[2];
	    //char line[1024];
		std::string _cmd;
		std::string _path;
		Request *_request;
		Server_config *_config;
	    std::stringstream buffer;
	public:
		Cgi(Request *request, Server_config *config);
		~Cgi();
		int checkCmdAndPath();
		void setEnvironment();
		void setArguments();
		int executeCgi(std::string &output,  std::string &body);
};
