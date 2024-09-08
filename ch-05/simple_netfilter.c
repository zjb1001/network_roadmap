#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/netfilter.h>
#include <linux/netfilter_ipv4.h>
#include <linux/ip.h>
#include <linux/tcp.h>

static struct nf_hook_ops nfho;

unsigned int hook_func(void *priv, struct sk_buff *skb, const struct nf_hook_state *state)
{
    struct iphdr *iph;
    struct tcphdr *tcph;

    iph = ip_hdr(skb);
    if (iph->protocol == IPPROTO_TCP) {
        tcph = tcp_hdr(skb);
        printk(KERN_INFO "Packet captured: %pI4:%d -> %pI4:%d\n",
               &iph->saddr, ntohs(tcph->source),
               &iph->daddr, ntohs(tcph->dest));
    }

    return NF_ACCEPT;
}

int init_module()
{
    nfho.hook = hook_func;
    nfho.hooknum = NF_INET_PRE_ROUTING;
    nfho.pf = PF_INET;
    nfho.priority = NF_IP_PRI_FIRST;

    nf_register_net_hook(&init_net, &nfho);
    printk(KERN_INFO "Simple Netfilter module loaded\n");
    return 0;
}

void cleanup_module()
{
    nf_unregister_net_hook(&init_net, &nfho);
    printk(KERN_INFO "Simple Netfilter module unloaded\n");
}

MODULE_LICENSE("GPL");