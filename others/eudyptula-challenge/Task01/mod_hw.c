#include <linux/module.h>    
#include <linux/kernel.h>    
#include <linux/init.h>      

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Jeremias Perez");
MODULE_DESCRIPTION("Task 01 - Hello world Module");

static int __init hw_init(void)
{
    printk(KERN_DEBUG "[LOADING] Hello world!\n");
    return 0;    // 0 is succesful return
}

static void __exit hw_cleanup(void)
{
    printk(KERN_DEBUG "[UNLOADING] Good bye!\n");
}

module_init(hw_init);
module_exit(hw_cleanup);

