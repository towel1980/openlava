/* $Id: lsf.h 397 2007-11-26 19:04:00Z mblack $
 * Copyright (C) 2007 Platform Computing Inc
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of version 2 of the GNU General Public License as
 * published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.

 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
 *
 */

#ifndef _LSF_H_
#define _LSF_H_
#include <stdio.h>

#include <unistd.h>
#include <syslog.h>
#include <sys/param.h>
#include <sys/time.h>
#include <sys/stat.h>
#include <sys/resource.h>

typedef long long int LS_LONG_INT;
typedef unsigned long long LS_UNS_LONG_INT;
#define LS_LONG_FORMAT ("%lld")


#include <sys/wait.h>

#if defined(__STDC__) 
#ifdef REL_DATE
#define _LS_VERSION_ ("Platform Lava 1.0, " REL_DATE "\nCopyright 2007 Platform Computing Corporation\n")
#else
#define _LS_VERSION_ ("Platform Lava 1.0, " __DATE__ "\nCopyright 2007 Platform Computing Corporation\n")
#endif
#else
#if defined(__DATE__)
#define _LS_VERSION_ ("Platform Lava 1.0, " __DATE__ "\nCopyright 2007 Platform Computing Corporation\n")
#else
#define _LS_VERSION_ ("Platform Lava 1.0 \nCopyright 2007 Platform Computing Corporation\n")
#endif 
#endif

#define LAVA_VERSION   1 	       
#define LSF_VERSION LAVA_VERSION
#define LAVA_XDR_VERSION1_0          1 	      

#define LAVA_CURRENT_VERSION   "1.0" 

#if defined(__STDC__)
#define P_(s) s
#include <stdarg.h>
#else
#define P_(s) ()
#include <varargs.h>
#endif


#define LSF_DEFAULT_SOCKS	15   
#define MAXLINELEN		512  
#define MAXLSFNAMELEN           40   

#define MAXSRES                 32   
#define MAXRESDESLEN            256  
#define NBUILTINDEX	        11   
#define MAXTYPES                128  
#define MAXMODELS               128  
#define MAXTYPES_31             25   
#define MAXMODELS_31            30   
#define MAXFILENAMELEN          256  
#define MAXEVARS                30   

#define GENMALLOCPACE           1024 

#define FIRST_RES_SOCK	20

#ifdef HAVE_UNION_WAIT
# define LS_WAIT_T	union wait
# define LS_STATUS(s)	((s).w_status)
#else
# define LS_WAIT_INT
# define LS_WAIT_T	int
# define LS_STATUS(s)	(s)
#endif


#define R15S           0
#define R1M            1
#define R15M           2
#define UT             3
#define PG             4
#define IO             5
#define LS             6
#define IT             7
#define TMP            8
#define SWP            9
#define MEM            10
#define USR1           11
#define USR2           12

#define INFINIT_LOAD    (float) (0x7fffffff)
#define INFINIT_FLOAT   (float) (0x7fffffff)

#define INFINIT_INT    0x7fffffff
#define INFINIT_LONG_INT    0x7fffffff

#define INFINIT_SHORT  0x7fff

#define DEFAULT_RLIMIT     -1

#define LSF_RLIMIT_CPU      0            
#define LSF_RLIMIT_FSIZE    1            
#define LSF_RLIMIT_DATA     2            
#define LSF_RLIMIT_STACK    3            
#define LSF_RLIMIT_CORE     4            
#define LSF_RLIMIT_RSS      5            
#define LSF_RLIMIT_NOFILE   6            
#define LSF_RLIMIT_OPEN_MAX 7            
#define LSF_RLIMIT_VMEM     8            
#define LSF_RLIMIT_SWAP     LSF_RLIMIT_VMEM
#define LSF_RLIMIT_RUN      9            
#define LSF_RLIMIT_PROCESS  10           
#define LSF_RLIM_NLIMITS    11           


#define LSF_NULL_MODE    0  
#define LSF_LOCAL_MODE   1
#define LSF_REMOTE_MODE  2

#define RF_MAXHOSTS 5

#define RF_CMD_MAXHOSTS 0
#define RF_CMD_RXFLAGS 2


#define STATUS_TIMEOUT        125      
#define STATUS_IOERR          124      
#define STATUS_EXCESS         123      
#define STATUS_REX_NOMEM      122      
#define STATUS_REX_FATAL      121      
#define STATUS_REX_CWD        120      
#define STATUS_REX_PTY        119      
#define STATUS_REX_SP         118      
#define STATUS_REX_FORK       117      
#define STATUS_REX_TOK        116      
#define STATUS_REX_UNKNOWN    115      
#define STATUS_REX_NOVCL      114      
#define STATUS_REX_NOSYM      113      
#define STATUS_REX_VCL_INIT   112      
#define STATUS_REX_VCL_SPAWN  111      
#define STATUS_REX_EXEC       110      
#define STATUS_REX_MLS_INVAL  109      
#define STATUS_REX_MLS_CLEAR  108      
#define STATUS_REX_MLS_RHOST  107      
#define STATUS_REX_MLS_DOMIN  106      

#define REX_FATAL_ERROR(s)     (((s) == STATUS_REX_NOVCL) \
                                 || ((s) == STATUS_REX_NOSYM) \
                                 || ((s) == STATUS_REX_NOMEM) \
                                 || ((s) == STATUS_REX_FATAL) \
                                 || ((s) == STATUS_REX_CWD) \
                                 || ((s) == STATUS_REX_PTY) \
                                 || ((s) == STATUS_REX_VCL_INIT) \
                                 || ((s) == STATUS_REX_VCL_SPAWN) \
                                 || ((s) == STATUS_REX_MLS_INVAL) \
                                 || ((s) == STATUS_REX_MLS_CLEAR) \
                                 || ((s) == STATUS_REX_MLS_RHOST) \
                                 || ((s) == STATUS_REX_MLS_DOMIN))

#define   REXF_USEPTY   0x00000001        
#define   REXF_CLNTDIR  0x00000002        
#define   REXF_TASKPORT 0x00000004        
#define   REXF_SHMODE   0x00000008        
#define   REXF_TASKINFO 0x00000010        
#define   REXF_REQVCL   0x00000020        
#define   REXF_SYNCNIOS 0x00000040        
#define   REXF_TTYASYNC	0x00000080        
#define   REXF_STDERR   0x00000100        

#define EXACT         0x01
#define OK_ONLY       0x02
#define NORMALIZE     0x04              
#define LOCALITY      0x08
#define IGNORE_RES    0x10
#define LOCAL_ONLY    0x20              
#define DFT_FROMTYPE  0x40		
#define ALL_CLUSTERS  0x80              
#define EFFECTIVE     0x100             
#define RECV_FROM_CLUSTERS 0x200
#define NEED_MY_CLUSTER_NAME 0x400

#define SEND_TO_CLUSTERS   0x400

#define FROM_MASTER   0x01

#define KEEPUID       0x01

#define RES_CMD_REBOOT          1           
#define RES_CMD_SHUTDOWN        2           
#define RES_CMD_LOGON           3
#define RES_CMD_LOGOFF          4

#define LIM_CMD_REBOOT          1
#define LIM_CMD_SHUTDOWN        2


struct connectEnt {                       
    char *hostname;
    int csock[2];
};

#define INTEGER_BITS       32  
#define GET_INTNUM(i) ((i)/INTEGER_BITS + 1)

#define LIM_UNAVAIL  0x00010000
#define LIM_LOCKEDU  0x00020000      
#define LIM_LOCKEDW  0x00040000      
#define LIM_BUSY     0x00080000      
#define LIM_RESDOWN  0x00100000      
#define LIM_LOCKEDM    0x00200000    

#define LIM_OK_MASK    0x00bf0000     

#define LIM_SBDDOWN    0x00400000    




#define LS_ISUNAVAIL(status)     (((status[0]) & LIM_UNAVAIL) != 0)

#define LS_ISBUSYON(status, index)  \
      (((status[1 + (index)/INTEGER_BITS]) & (1 << (index)%INTEGER_BITS)) != 0)

#define LS_ISBUSY(status) (((status[0]) & LIM_BUSY) != 0)

#define LS_ISLOCKEDU(status)   (((status[0]) & LIM_LOCKEDU) != 0)

#define LS_ISLOCKEDW(status)   (((status[0]) & LIM_LOCKEDW) != 0)

#define LS_ISLOCKEDM(status)   (((status[0]) & LIM_LOCKEDM) != 0)

#define LS_ISLOCKED(status)    (((status[0]) & (LIM_LOCKEDU | LIM_LOCKEDW | LIM_LOCKEDM)) != 0) 

#define LS_ISRESDOWN(status)   (((status[0]) & LIM_RESDOWN) != 0)

#define LS_ISSBDDOWN(status)   (((status[0]) & LIM_SBDDOWN) != 0)

#define LS_ISOK(status)  ((status[0] & LIM_OK_MASK) == 0)


#define LS_ISOKNRES(status) (((status[0]) & ~(LIM_RESDOWN | LIM_SBDDOWN)) == 0)

struct placeInfo {          
   char  hostName[MAXHOSTNAMELEN];
   int   numtask;
};

struct hostLoad {           
   char  hostName[MAXHOSTNAMELEN];
   int   *status;
   float *li;
};

enum valueType {LS_BOOLEAN, LS_NUMERIC, LS_STRING, LS_EXTERNAL};
#define BOOLEAN  LS_BOOLEAN
#define NUMERIC  LS_NUMERIC
#define STRING   LS_STRING
#define EXTERNAL LS_EXTERNAL
enum orderType {INCR, DECR, NA};

#define RESF_BUILTIN     0x01    
#define RESF_DYNAMIC     0x02    
#define RESF_GLOBAL      0x04    
#define RESF_SHARED      0x08    
#define RESF_EXTERNAL    0x10    
#define RESF_RELEASE     0x20    
#define RESF_DEFINED_IN_RESOURCEMAP  0x40 
					  


struct resItem {
    char name[MAXLSFNAMELEN];	 
    char des[MAXRESDESLEN];      
    enum valueType valueType;    
    enum orderType orderType;    
    int  flags;                  
    int  interval;               
};

struct lsInfo {            
    int    nRes;
    struct resItem *resTable;
    int    nTypes;
    char   hostTypes[MAXTYPES][MAXLSFNAMELEN]; 
    int    nModels;
    char   hostModels[MAXMODELS][MAXLSFNAMELEN]; 
    char   hostArchs[MAXMODELS][MAXLSFNAMELEN];  
    int    modelRefs[MAXMODELS]; 
    float  cpuFactor[MAXMODELS];
    int    numIndx;          
    int    numUsrIndx;       
};

#define CLUST_STAT_OK             0x01
#define CLUST_STAT_UNAVAIL        0x02

struct clusterInfo {
    char  clusterName[MAXLSFNAMELEN];
    int   status;
    char  masterName[MAXHOSTNAMELEN];
    char  managerName[MAXLSFNAMELEN];
    int   managerId;
    int   numServers;      
    int   numClients;      
    int   nRes;            
    char  **resources;     
    int    nTypes;
    char **hostTypes;      
    int    nModels;       
    char **hostModels;     
    int    nAdmins;        
    int  *adminIds;        
    char **admins;         
};

struct hostInfo {
    char  hostName[MAXHOSTNAMELEN];
    char  *hostType;
    char  *hostModel;
    float cpuFactor;
    int   maxCpus;
    int   maxMem;
    int   maxSwap;
    int   maxTmp; 
    int   nDisks;
    int   nRes;
    char  **resources;
    char  *windows;		
    int   numIndx;
    float *busyThreshold;	
    char  isServer;
    int   rexPriority;
};

struct config_param {          
    char *paramName;
    char *paramValue;
};


struct	lsfRusage {
	double ru_utime;	        
	double ru_stime;	        
	double	ru_maxrss;
	double	ru_ixrss;		
	double	ru_ismrss;	 
	double	ru_idrss;		
	double	ru_isrss;		
	double	ru_minflt;		
	double	ru_majflt;		
	double	ru_nswap;		
	double	ru_inblock;		
	double	ru_oublock;		
	double  ru_ioch;         
	double	ru_msgsnd;		
	double	ru_msgrcv;		
	double	ru_nsignals;		
	double	ru_nvcsw;		
	double	ru_nivcsw;		
	double  ru_exutime;      
};


struct lsfAcctRec {
    int pid;
    char *username;
    int exitStatus;
    time_t dispTime;
    time_t termTime;
    char *fromHost;
    char *execHost;
    char *cwd;
    char *cmdln;
    struct lsfRusage lsfRu;
};



#define NIO_STDIN_ON                        0x01 
#define NIO_STDIN_OFF                       0x02 
#define NIO_TAGSTDOUT_ON                    0x03 
#define NIO_TAGSTDOUT_OFF                   0x04 

#define NIO_TASK_STDINON                    0x01 
#define NIO_TASK_STDINOFF                   0x02 
#define NIO_TASK_ALL                        0x03 
#define NIO_TASK_CONNECTED                  0x04 

enum nioType {
    NIO_STATUS,                        
    NIO_STDOUT,                        
    NIO_EOF,                           
    NIO_IOERR,                         
    NIO_REQUEUE,       		       
    NIO_STDERR                         
};

struct nioEvent {
    int tid;                    
    enum nioType type;          
    int status;                 
};

struct nioInfo {
    int num;                    
    struct nioEvent *ioTask;
};



struct confNode {
    struct confNode *leftPtr;	
    struct confNode *rightPtr;	
    struct confNode *fwPtr;	
    char	*cond;		
    int		beginLineNum;	
    int		numLines;	
    char	**lines;	
    char	tag;		
};

struct pStack {
    int top;
    int size;
    struct confNode **nodes;
};

struct confHandle {
    struct confNode *rootNode;	
    char        *fname;		
    struct confNode *curNode;	 
    int		lineCount;	
    struct pStack *ptrStack;	
};

struct lsConf {
    struct confHandle *confhandle;	
    int         numConds;		
    char        **conds;		
    int		*values;		
};

struct sharedConf {
    struct lsInfo *lsinfo;
    char	*clusterName;
    char 	*servers;
};

typedef struct lsSharedResourceInstance {
    char *value;        
    int  nHosts;        
    char **hostList;

} LS_SHARED_RESOURCE_INST_T;

typedef struct lsSharedResourceInfo {
    char *resourceName;  
    int  nInstances;     
    LS_SHARED_RESOURCE_INST_T  *instances;    
} LS_SHARED_RESOURCE_INFO_T;

struct clusterConf {
    struct clusterInfo *clinfo;
    int       numHosts;
    struct hostInfo *hosts;
    int numShareRes;
    LS_SHARED_RESOURCE_INFO_T *shareRes;
};



struct pidInfo {
    int pid;          
    int ppid;          
    int pgid;         
    int jobid;        
}; 

struct jRusage {
    int mem;          
    int swap;         
    int utime;        
    int stime;        
    int npids;        
    struct pidInfo *pidInfo; 
                      
    int npgids;       
    int *pgid;        
};



#define LSE_NO_ERR              0     
#define LSE_BAD_XDR             1     
#define LSE_MSG_SYS             2     
#define LSE_BAD_ARGS            3     
#define LSE_MASTR_UNKNW         4     
#define LSE_LIM_DOWN            5     
#define LSE_PROTOC_LIM          6     
#define LSE_SOCK_SYS            7     
#define LSE_ACCEPT_SYS          8     
#define LSE_BAD_TASKF           9     
#define LSE_NO_HOST             10    
#define LSE_NO_ELHOST           11    
#define LSE_TIME_OUT            12    
#define LSE_NIOS_DOWN           13    
#define LSE_LIM_DENIED          14    
#define LSE_LIM_IGNORE          15    
#define LSE_LIM_BADHOST         16    
#define LSE_LIM_ALOCKED         17    
#define LSE_LIM_NLOCKED         18    
#define LSE_LIM_BADMOD          19    
#define LSE_SIG_SYS             20    
#define LSE_BAD_EXP             21    
#define LSE_NORCHILD            22    
#define LSE_MALLOC              23    
#define LSE_LSFCONF             24    
#define LSE_BAD_ENV             25    
#define LSE_LIM_NREG            26    
#define LSE_RES_NREG            27    
#define LSE_RES_NOMORECONN      28    
#define LSE_BADUSER             29    
#define LSE_RES_ROOTSECURE      30    
#define LSE_RES_DENIED          31    
#define LSE_BAD_OPCODE          32    
#define LSE_PROTOC_RES          33    
#define LSE_RES_CALLBACK        34    
#define LSE_RES_NOMEM           35    
#define LSE_RES_FATAL           36    
#define LSE_RES_PTY             37    
#define LSE_RES_SOCK            38    
#define LSE_RES_FORK            39    
#define LSE_NOMORE_SOCK         40    
#define LSE_WDIR                41    
#define LSE_LOSTCON             42    
#define LSE_RES_INVCHILD        43    
#define LSE_RES_KILL            44    
#define LSE_PTYMODE             45    
#define LSE_BAD_HOST            46    
#define LSE_PROTOC_NIOS         47    
#define LSE_WAIT_SYS            48    
#define LSE_SETPARAM            49    
#define LSE_RPIDLISTLEN         50    
#define LSE_BAD_CLUSTER         51    
#define LSE_RES_VERSION         52    
#define LSE_EXECV_SYS           53    
#define LSE_RES_DIR             54    
#define LSE_RES_DIRW            55    
#define LSE_BAD_SERVID          56    
#define LSE_NLSF_HOST           57    
#define LSE_UNKWN_RESNAME       58    
#define LSE_UNKWN_RESVALUE      59    
#define LSE_TASKEXIST           60    
#define LSE_BAD_TID             61    
#define LSE_TOOMANYTASK         62    
#define LSE_LIMIT_SYS           63    
#define LSE_BAD_NAMELIST        64    
#define LSE_LIM_NOMEM           65    
#define LSE_NIO_INIT            66    
#define LSE_CONF_SYNTAX         67    
#define LSE_FILE_SYS            68    
#define LSE_CONN_SYS            69    
#define LSE_SELECT_SYS          70    
#define LSE_EOF                 71    
#define LSE_ACCT_FORMAT         72    
#define LSE_BAD_TIME            73    
#define LSE_FORK                74    
#define LSE_PIPE                75    
#define LSE_ESUB                76    
#define LSE_EAUTH               77    
#define LSE_NO_FILE             78    
#define LSE_NO_CHAN             79    
#define LSE_BAD_CHAN            80    
#define LSE_INTERNAL            81    
#define LSE_PROTOCOL            82    
#define LSE_MISC_SYS            83    
#define LSE_RES_RUSAGE          84    
#define LSE_NO_RESOURCE         85    
#define LSE_BAD_RESOURCE        86    
#define LSE_RES_PARENT          87    
#define LSE_I18N_SETLC          88    
#define LSE_I18N_CATOPEN        89    
#define LSE_I18N_NOMEM          90    
#define LSE_NO_MEM              91    
#define LSE_FILE_CLOSE          92    
#define LSE_LIMCONF_NOTREADY    93    
#define LSE_MASTER_LIM_DOWN     94    
#define LSE_MLS_INVALID         95    
#define LSE_MLS_CLEARANCE       96    
#define LSE_MLS_RHOST           97    
#define LSE_MLS_DOMINATE        98    
#define LSE_NERR                98    


#define LSE_ISBAD_RESREQ(s)	(((s) == LSE_BAD_EXP) \
				 || ((s) == LSE_UNKWN_RESNAME) \
				 || ((s) == LSE_UNKWN_RESVALUE))

#define LSE_SYSCALL(s)          (((s) == LSE_SELECT_SYS) \
				 || ((s) == LSE_CONN_SYS) \
				 || ((s) == LSE_FILE_SYS) \
				 || ((s) == LSE_MSG_SYS) \
				 || ((s) == LSE_SOCK_SYS) \
				 || ((s) == LSE_ACCEPT_SYS) \
				 || ((s) == LSE_SIG_SYS) \
				 || ((s) == LSE_WAIT_SYS) \
				 || ((s) == LSE_EXECV_SYS) \
				 || ((s) == LSE_LIMIT_SYS) \
				 || ((s) == LSE_PIPE) \
				 || ((s) == LSE_ESUB) \
				 || ((s) == LSE_MISC_SYS))

#define TIMEIT(level,func,name) \
                    { if (timinglevel > level) { \
                          struct timeval before, after; \
                          struct timezone tz; \
                          gettimeofday(&before, &tz); \
                          func; \
                          gettimeofday(&after, &tz); \
                          ls_syslog(LOG_INFO,"L%d %s %d ms",level,name, \
                              (int)((after.tv_sec - before.tv_sec)*1000 + \
                               (after.tv_usec-before.tv_usec)/1000)); \
                       } else \
                              func; \
                    }
                    

#define TIMEVAL(level,func,val) \
                    { if (timinglevel > level) { \
                          struct timeval before, after; \
                          struct timezone tz; \
                          gettimeofday(&before, &tz); \
                          func; \
                          gettimeofday(&after, &tz); \
                          val = (int)((after.tv_sec - before.tv_sec)*1000 + \
                               (after.tv_usec-before.tv_usec)/1000); \
                       } else { \
                              func; \
                              val = 0; \
                         } \
                    }

#define LC_SCHED    0x00000001 
#define LC_EXEC     0x00000002 
#define LC_TRACE    0x00000004 
#define LC_COMM     0x00000008 
#define LC_XDR      0x00000010 
#define LC_CHKPNT   0x00000020 
#define LC_FILE     0x00000080 
#define LC_AUTH     0x00000200 
#define LC_HANG     0x00000400 
#define LC_SIGNAL   0x00001000 
#define LC_PIM      0x00004000 
#define LC_SYS      0x00008000 
#define LC_JLIMIT   0x00010000 
#define LC_PEND     0x00080000 
#define LC_LOADINDX 0x00200000 
#define LC_JGRP     0x00400000 
#define LC_JARRAY   0x00800000 
#define LC_MPI      0x01000000 
#define LC_ELIM     0x02000000 
#define LC_M_LOG    0x04000000 
#define LC_PERFM    0x08000000 

#define LOG_DEBUG1  LOG_DEBUG + 1  
#define LOG_DEBUG2  LOG_DEBUG + 2  
#define LOG_DEBUG3  LOG_DEBUG + 3

#define LSF_NIOS_REQUEUE	127 



extern int     lserrno;
extern int     masterLimDown; 
extern int     ls_nerr;
extern char    *ls_errmsg[];
extern int     logclass;
extern int     timinglevel;

extern int     lsf_lim_version;	
extern int     lsf_res_version;	

extern int     ls_initrex P_((int, int));
#define ls_init(a, b) ls_initrex((a), (b))  

extern int     ls_readconfenv P_((struct config_param *, char *));
extern int     ls_connect P_((char *));
extern int     ls_rexecv P_((char *, char **, int));
extern int     ls_rexecve P_((char *, char **, int, char **));
extern int     ls_rtask P_((char *, char **, int));
extern int     ls_rtaske P_((char *, char **, int, char **));
extern int     ls_rwait P_((LS_WAIT_T *, int, struct rusage *));
extern int     ls_rwaittid P_((int, LS_WAIT_T *, int, struct rusage *));
extern int     ls_rkill P_((int, int));
extern int     ls_startserver P_((char *, char **, int));
extern int     ls_conntaskport P_((int tid));    

extern char    **ls_placereq P_((char *resreq, int *numhosts, int options,
				char *fromhost));
extern char    **ls_placeofhosts P_((char *resreq, int *numhosts, 
                                int options, char *fromhost, char **hostlist, 
                                int listsize));
extern char    **ls_placeoftype P_((char *resreq, int *numhosts, 
                                int options, char *fromhost, char *hosttype));
extern struct  hostLoad *ls_load P_((char *resreq, int *numhosts, int options,
				char *fromhost));
extern struct  hostLoad *ls_loadofhosts P_((char *resreq, int *numhosts,
				int options, char *fromhost, char **hostlist,
				int listsize));
extern struct  hostLoad *ls_loadoftype P_((char *resreq, int *numhosts,
				int options, char *fromhost, char *hosttype));
extern struct  hostLoad *ls_loadinfo P_((char *resreq, int *numhosts, 
				int options, char *fromhost, char **hostlist, 
			        int listsize, char ***indxnamelist));
extern int     ls_loadadj P_((char *resreq, struct placeInfo *hostlist, 
                             int listsize));
extern int     ls_eligible P_((char *task, char *resreqstr, char mode));
extern char *  ls_resreq P_((char *task));
extern int     ls_insertrtask P_((char *task));
extern int     ls_insertltask P_((char *task));
extern int     ls_deletertask P_((char *task));
extern int     ls_deleteltask P_((char *task));
extern int     ls_listrtask P_((char ***taskList, int sortflag));
extern int     ls_listltask P_((char ***taskList, int sortflag));
extern char ** ls_findmyconnections P_((void));
extern int     ls_isconnected P_((char *hostName));
extern int     ls_lostconnection P_((void));
extern char    *ls_getclustername P_((void));
extern struct clusterInfo *ls_clusterinfo P_((char *, int *, char **, int, int));
extern struct lsSharedResourceInfo *ls_sharedresourceinfo P_((char **, int *, char *, int));
extern char    *ls_getmastername P_((void));
extern char    *ls_getmyhostname P_((void));
extern struct  hostInfo *ls_gethostinfo P_((char *, int *, char **, int, int));
extern char    *ls_getISVmode P_((void));

extern struct  lsInfo    *ls_info P_((void));

extern char ** ls_indexnames P_((struct lsInfo *)); 
extern int     ls_isclustername P_((char *)); 
extern char    *ls_gethosttype P_((char *hostname));
extern float   *ls_getmodelfactor P_((char *modelname));
extern float   *ls_gethostfactor P_((char *hostname));
extern char    *ls_gethostmodel P_((char *hostname));
extern int     ls_lockhost P_((time_t duration));
extern int     ls_unlockhost P_((void));
extern int     ls_limcontrol P_((char *hostname, int opCode));    
extern void    ls_remtty P_((int ind, int enableIntSus));
extern void    ls_loctty P_((int ind));
extern char    *ls_sysmsg P_((void));
extern void    ls_perror P_((char *usrMsg));


extern struct lsConf *ls_getconf P_((char *));
extern void ls_freeconf P_((struct lsConf * ));
extern struct sharedConf *ls_readshared P_((char *));
extern struct clusterConf *ls_readcluster P_((char *, struct lsInfo *));
extern struct clusterConf *ls_readcluster_ex P_((char *, struct lsInfo *, int));


extern int     ls_initdebug P_((char *appName));
extern void    ls_syslog P_((int level, const char *fmt, ...))
#if defined (__GNUC__) && defined (CHECK_ARGS)  
    __attribute__((format(printf, 2, 3)))
#endif  
        ;

extern void	ls_errlog P_((FILE *fp, const char *fmt, ...))
#if defined (__GNUC__) && defined (CHECK_ARGS) 	
	__attribute__((format(printf, 2, 3)))
#endif  
	;
extern void	ls_verrlog P_((FILE *fp, const char *fmt, va_list ap));

extern int	ls_rescontrol P_((char *host, int opcode, int options));
extern int	ls_stdinmode P_((int onoff));
extern int      ls_stoprex P_((void));
extern int	ls_donerex P_((void));
extern int	ls_rsetenv P_((char *host, char **env));
extern int	ls_rsetenv_async P_((char *host, char **env));
extern int	ls_setstdout P_((int on, char *format));
extern int	ls_niossync P_((int));
extern int	ls_setstdin P_((int on, int *rpidlist, int len));
extern int      ls_chdir P_((char *, char *));
extern int      ls_fdbusy P_((int fd));
extern char     *ls_getmnthost P_((char *fn));    
extern int      ls_servavail P_((int, int));
extern int	ls_setpriority P_((int newPriority));
    
extern int ls_ropen P_((char *host, char *fn, int flags, int mode));
extern int ls_rclose P_((int rfd));
extern int ls_rwrite P_((int rfd, char *buf, int len));
extern int ls_rread P_((int rfd, char *buf, int len));
extern off_t ls_rlseek P_((int rfd, off_t offset, int whence));
extern int ls_runlink P_((char *host, char *fn));
extern int ls_rfstat P_((int rfd, struct stat *buf));
extern int ls_rstat P_((char *host, char *fn, struct stat *buf));
extern char *ls_rgetmnthost P_((char *host, char *fn));
extern int ls_rfcontrol P_((int command, int arg));
extern int ls_rfterminate P_((char *host));

extern void ls_ruunix2lsf P_((struct rusage *rusage, struct lsfRusage *lsfRusage));
extern void ls_rulsf2unix P_((struct lsfRusage *lsfRusage, struct rusage *rusage));
extern void cleanLsfRusage P_((struct lsfRusage *));
extern void cleanRusage P_((struct rusage *));

extern struct resLogRecord *ls_readrexlog P_((FILE *));
extern int     ls_nioinit P_((int sock));
extern int     ls_nioselect P_((int, fd_set *, fd_set *, fd_set *, struct nioInfo ** , struct timeval *)); 
extern int     ls_nioctl P_((int, int));
extern int     ls_nionewtask P_((int, int));
extern int     ls_nioremovetask P_((int));
extern int     ls_niowrite P_((char *, int));
extern int     ls_nioclose P_((void));
extern int     ls_nioread P_((int, char *, int));
extern int     ls_niotasks P_((int, int *, int));
extern int     ls_niostatus P_((int, int *, struct rusage *));
extern int     ls_niokill P_((int));
extern int     ls_niosetdebug P_((int));
extern int     ls_niodump P_((int, int, int, char *));

extern struct lsfAcctRec *ls_getacctrec P_((FILE *, int *));
extern int ls_putacctrec P_((FILE *, struct lsfAcctRec *));
extern int getBEtime P_((char *, char, time_t *));

#ifndef NON_ANSI
typedef int (*exceptProto)(void);

struct extResInfo {
    char *name;         
    char *type;         
    char *interval;     
    char *increasing;   
    char *des;          
};

extern void  *ls_handle P_((void));
extern int   ls_catch P_((void *handle, char *key, exceptProto func));
extern int   ls_throw P_((void *handle, char *key));
extern char  *ls_sperror P_((char *usrMsg));

#endif 
#undef P_

#endif
