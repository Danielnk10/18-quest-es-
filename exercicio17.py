main() {
float ar,lt,qlg,qlp,vglg,rp,rg,vglp;
    
    printf("Informe o tamanho, em metros quadrados, da área a ser pintada:");
    scanf("%f",&ar);
    
    lt=ar/6;
    qlg=lt/18;
    vglg=qlg*80;
    qlp=lt/3.6;
    vglp=qlp*25;
    
    printf("\n Quantidade de litros necessarios: %.2f.",lt);
    printf("\n Quantidade de latas de 18 litros: %.2f e valor gasto: %.2f.",qlg,vglg);
    printf("\n Quantidade de latas de 3,6 litros: %.2f e valor gasto: %.2f.",qlp,vglp);
    rg=lt/18;
    rp=(ar-(rg*108))/21.6;
    
    printf("\n Latas Grandes %.2f e latas pequenas %.2f.",rg,rp);
}